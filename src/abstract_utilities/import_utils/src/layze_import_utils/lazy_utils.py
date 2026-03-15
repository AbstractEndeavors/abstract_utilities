from ...imports import *
from .nullProxy import nullProxy,nullProxy_logger
from ..import_utils import inject_from_imports_map,get_imports
import importlib,importlib.util, pkgutil,sys
from pathlib import Path


def dynamic_import(target: str | Path):
    """
    Import module/package/file dynamically.
    Returns module or nullProxy if unavailable.
    """
    try:
        p = Path(target)

        # file import
        if p.exists():
            name = f"_dyn_{p.stem}_{hash(p)}"

            spec = importlib.util.spec_from_file_location(name, str(p))
            if spec is None or spec.loader is None:
                raise ImportError(target)

            mod = importlib.util.module_from_spec(spec)
            sys.modules[name] = mod
            spec.loader.exec_module(mod)

            return mod

        # module import
        return importlib.import_module(target)

    except Exception:
        return nullProxy(str(target))
def safe_attr(obj, attr):
    try:
        return getattr(obj, attr)
    except Exception:
        return nullProxy(f"{obj}.{attr}")
@lru_cache(maxsize=None)
def lazy_import_single(name: str,fallback=None):
    """
    Import module safely. If unavailable, return NullProxy.
    """

    if name in sys.modules:
        return sys.modules[name]

    try:
        module = importlib.import_module(name)
        return module
    except Exception as e:
        nullProxy_logger.warning(
            "[lazy_import] Failed to import '%s': %s",
            name,
            e,
        )
        return nullProxy(name,fallback=fallback)

def get_lazy_attr(module_name: str, *attrs,fallback=None):
    obj = lazy_import(module_name,fallback=fallback)

    for attr in attrs:
        try:
            obj = getattr(obj, attr)
        except Exception:
            return nullProxy(module_name, attrs,fallback=fallback)

    return obj
def lazy_import(name: str, *attrs,fallback=None):
    """
    Import module safely. If unavailable, return NullProxy.
    """
    if attrs:
        obj = get_lazy_attr(name, *attrs,fallback=fallback)
    else:
        obj = lazy_import_single(name,fallback=fallback)
    return obj
def lazy_import_star(files, *, self=None):
    imports_map = get_imports(files)

    return inject_from_imports_map(
        imports_map,
        into=globals(),
        self=self
    )
def dynamic_star(pkg_name: str, *, into=None, self=None):
    """
    Import all public functions/classes from package modules.
    Optionally bind methods to `self`.
    """
    import inspect
    from types import MethodType

    ns = into if into else globals()
    exported = {}

    pkg = dynamic_import(pkg_name)

    try:
        modules = pkgutil.iter_modules(pkg.__path__)
    except Exception:
        return exported

    for _, modname, _ in modules:

        mod = dynamic_import(f"{pkg_name}.{modname}")

        for name, obj in vars(mod).items():

            if name.startswith("_"):
                continue

            if inspect.isfunction(obj):

                params = list(inspect.signature(obj).parameters.values())

                if self and params and params[0].name == "self":
                    bound = MethodType(obj, self)
                    setattr(self, name, bound)
                    exported[name] = bound
                else:
                    ns[name] = obj
                    exported[name] = obj

            elif inspect.isclass(obj):
                ns[name] = obj
                exported[name] = obj

    return exported
