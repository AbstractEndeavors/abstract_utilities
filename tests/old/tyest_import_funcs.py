from src.abstract_utilities import *
##import ast, os
##from pathlib import Path
##from textwrap import indent
##
##def find_py_files(root: Path):
##    for p in root.rglob("*.py"):
##        if "__pycache__" not in p.parts:
##            yield p
##
##def collect_imports(root: Path):
##    all_imports = set()
##    for file in find_py_files(root):
##        src = file.read_text(errors="ignore")
##        tree = ast.parse(src, filename=str(file))
##        for node in ast.walk(tree):
##            if isinstance(node, ast.Import):
##                for alias in node.names:
##                    all_imports.add(alias.name)
##            elif isinstance(node, ast.ImportFrom):
##                if node.module:
##                    all_imports.add(node.module)
##    return sorted(all_imports)
##
##def build_master_imports(package_root: Path, out_path: Path):
##    imports = collect_imports(package_root)
##    lines = ["# Auto-generated master imports\n"]
##    for name in imports:
##        # skip stdlib or external packages
##        if not name.startswith(package_root.name):
##            continue
##        rel_name = name[len(package_root.name)+1:] if name != package_root.name else ""
##        lines.append(f"from .{rel_name} import *" if rel_name else f"import {name}")
##    out_path.parent.mkdir(parents=True, exist_ok=True)
##    out_path.write_text("\n".join(lines))
##    print(f"✅ Generated master imports file at {out_path}")
##path="/home/flerb/Documents/pythonTools/modules/src/modules/abstract_utilities/src/abstract_utilities/import_utils/src/import_functions.py"
##
##import_data =get_imports(path)
##build_master_imports(import_data.get('sysroot'), os.path.join(os.getcwd(),'wow.py'))
##
##
logger = get_logFile(__name__)
logger.info('hihihi')
