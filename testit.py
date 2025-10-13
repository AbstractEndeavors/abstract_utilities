from src.abstract_utilities.file_utils.file_utils.file_utils import *
directory = "/home/computron/Documents/pythonTools/modules/src/modules/abstract_ide/src/abstract_ide/consoles/apiTab/functions"
SITES_AVAILABLE_PATH = "/etc/systemd/system/"
def normalize_items(
    paths: Iterable[str],
    user_at_host=None,
    get_type=True,
    get_is_dir=False,
    get_is_file=False,
    get_is_exists=False,
    **kwargs
) -> List[tuple[PathBackend, str, dict]]:
    pairs: List[tuple[PathBackend, str, dict]] = []
    host = user_at_host or kwargs.get("host") or kwargs.get("user")
    paths = make_list(paths)
    for item in paths:
        if not item:
            continue

        strings = try_group(REMOTE_RE, item, ["host", "path"])
        fs_host = None
        nuhost = None

        if (strings and None not in strings) or host:
            if strings and None not in strings:
                nuhost = strings[0]
                item = strings[1] or item
            nuhost = nuhost or host
            fs_host = SSHFS(
                nuhost,
                user_at_host=user_at_host,
                get_type=get_type,
                get_is_dir=get_is_dir,
                get_is_file=get_is_file,
                get_is_exists=get_is_exists,
                **kwargs
            )
        else:
            fs_host = LocalFS(
                get_type=get_type,
                get_is_dir=get_is_dir,
                get_is_file=get_is_file,
                get_is_exists=get_is_exists
            )

        includes = fs_host.is_included(item)
        pairs.append((fs_host, item, includes))
    return pairs
##out = get_files_and_dirs("/home/solcatcher",add=True) # returns text
file_paths = normalize_items(SITES_AVAILABLE_PATH)
input(file_paths)
for fs, root, _ in file_paths:
    input(fs)
    nu_items = fs.glob_recursive(root)
    input(nu_items)
input(file_paths)
file_paths = run_cmd('ls',cwd=SITES_AVAILABLE_PATH,user_at_host='solcatcher')
normalize_items(roots, **kwargs)
file_paths = get_files_and_dirs(SITES_AVAILABLE_PATH,allowed_exts=['.service'],add=True,user_at_host='solcatcher')
input(file_paths)

print(out)
# capture locally
out = get_files_and_dirs("/etc/nginx/sites-available",add=True) # returns text
print(out)
# capture on remote
out = cmd_run("ls -la /", user_at_host="solcatcher@23.126.105.154")
print(out)
# sudo capture locally
out = cmd_run_sudo("ls -la /", password="1")
print(out)
out = cmd_run("ls -la /", user_at_host="solcatcher")
print(out)
# sudo capture remote
out = cmd_run("reload_nginx", user_at_host="solcatcher")
print(out)
# legacy file-backed (works as before)
ourput = cmd_run("ls", user_at_host="solcatcher", print_output=True)
print(f'''cmd_run("ls", user_at_host="solcatcher", print_output=True) === {ourput}''')
ourput = cmd_run_sudo("echo hello", user_at_host="solcatcher", key="SUDO_PASSWORD", output_text="/tmp/upgrade.out")
print(ourput)
