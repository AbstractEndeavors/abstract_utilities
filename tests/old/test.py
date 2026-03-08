from src.abstract_utilities import *
def get_shortest(*items):
    shortest=[None,None]
    for item in items:
        len_item = len(item)
        if None in shortest or shortest[0] > len_item:
            shortest = [len_item,item]
    return shortest[-1]     
def get_path_parts(path):
    path_parts=[]
    if path and path[0] == '/':
        path_parts=['/']
    path_spl = path.split('/')
    
    path_parts += [part for part in path_spl if part]
    return path_parts
def find_commonn_root(*paths):
    all_path_parts = []
    for path in paths:
        all_path_parts.append(get_path_parts(path))
    shortest_item = get_shortest(*all_path_parts)
    common_path = []
    for i in range(len(shortest_item)):
        in_all = True
        current_path_part = None
        for path_parts in all_path_parts:
            path_part = path_parts[i]
            if current_path_part == None:
                current_path_part = path_part
            if current_path_part != path_part:
               in_all = False
               break
        if in_all == False:
            break
        else:
            common_path.append(current_path_part)
    return os.path.join(*common_path)
def get_dotted(main_path,sub_path):
    targetname = os.path.basename(main_path)
    if os.path.isfile(main_path):
        targetname,ext = os.path.splitext(targetname)
    main_dirname = os.path.dirname(main_path)
    sub_dirname = os.path.dirname(sub_path)
    common_path = find_commonn_root(main_dirname,sub_dirname)
    sub_rel_dirname = sub_dirname.split(common_path)[-1]
    sub_rel_dir_parts = get_path_parts(sub_rel_dirname)
    dots = ''
    for i in range(len(sub_rel_dir_parts)):
        dots+='.'
    return f"{dots}{targetname}"
IMPORT_STR = 'import '
main_import = '/home/flerb/Documents/pythonTools/modules/src/modules/abstract_utilities/src/abstract_utilities/imports.py'
directory = "/home/flerb/Documents/pythonTools/modules/src/modules/abstract_utilities/src"
dirs,files = get_files_and_dirs(directory,allowed_patterns = 'imports',allowed_exts='.py')
for file in files:
    dotted = get_dotted(main_import,file)
    if file != main_import:
        contents = read_from_file(file)
        lines = contents.split('\n')
        for i,line in enumerate(lines):
            if line.startswith(IMPORT_STR):
               nuline = line[len(IMPORT_STR):]
               line = f"from {dotted} {IMPORT_STR}{nuline}"
            lines[i]=line
        contents ='\n'.join(lines)
        write_to_file(contents=contents,file_path=file)

