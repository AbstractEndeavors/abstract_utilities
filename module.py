import os,ast,sys,re,pkg_resources
def scan_folder_for_required_modules(folder_path=None,exclude:(str or list)=[],exclue_default_modules:bool=True):
    """
    Scan the specified folder for Python files and create a list of necessary Python modules.
    :param folder_path: The path of the folder to scan. If None, a folder will be picked using a GUI window.
    :return: A list of required Python modules based on all Python files found in the folder.
    """
    exclude=list(exclude)
    if folder_path is None:
        folder_path = get_browser(
            title="Please choose the destination for your import scripts to be analyzed",
            initial_folder=os.getcwd()
        )
    
    required_modules = set()

    def visit_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                tree = ast.parse(file.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.Import):
                        for name in node.names:
                            required_modules.add(name.name)
                    elif isinstance(node, ast.ImportFrom):
                        try:
                            module_parts = node.module.split('.')
                            if node.level > 0:
                                module_parts = ['.'.join(module_parts[:node.level])] + module_parts[node.level:]
                            module_name = '.'.join(module_parts)
                            for name in node.names:
                                required_modules.add(f'{module_name}.{name.name}')
                        except:
                            pass
        except SyntaxError:
            # Skip files with syntax errors
            pass

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                visit_file(file_path)
       
    # Update the required_modules to include submodules
    updated_required_modules = set()
    for module in required_modules:
        if module not in exclude:
            parts = module.split('.')
            for i in range(len(parts)):
                updated_required_modules.add('.'.join(parts[:i+1]))
    if exclue_default_modules:
        new_modules = []
        for each in updated_required_modules:
            if each not in sys.builtin_module_names:
                new_modules.append(each)
        updated_required_modules =new_modules
    required_list = list(updated_required_modules)
    return required_list
def is_valid_package_name(package_name):
    # Python package names must start with a letter and can only contain ASCII letters, numbers, and underscores
    return re.match(r'^[a-zA-Z][a-zA-Z0-9_]*$', package_name) is not None

def get_installed_versions(install_requires):
    """
    Get the version numbers of the installed Python modules listed in 'install_requires'.
    :param install_requires: A list of Python module names with optional version constraints.
    :return: A list of module names with their version numbers appended.
    """
    installed_versions = []
    for requirement in install_requires:
        module_name = requirement.split('>=')[0].split('==')[0].strip()
        
        # Validate module_name and skip if not valid
        if not is_valid_package_name(module_name):
            continue

        try:
            version = pkg_resources.get_distribution(module_name).version
        except pkg_resources.DistributionNotFound:
            # Module not found, skip it and continue
            continue

        # Append the version number to the module name in the required format
        if '>=' in requirement:
            installed_versions.append(f'{module_name}>={version}')
        elif '==' in requirement:
            installed_versions.append(f'{module_name}=={version}')
        else:
            installed_versions.append(f'{module_name}>={version}')

    return installed_versions

input(get_installed_versions(scan_folder_for_required_modules("C:/Users/jrput/Documents/python projects/Modules/abstract_utilities/src/abstract_utilities")))
