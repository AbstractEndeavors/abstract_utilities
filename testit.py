from src.abstract_utilities import *
directory = "/var/www/api/abstract_logins/abstract_login/src/abstract_logins/app/imports/src/auth_utils/user_store/admin_utils/create_user.py"
froms = extract_froms(directory)
imports = extract_imports(directory)
funcs = extract_funcs(directory)
classes = extract_class(directory)
out = get_files_and_dirs("/home/solcatcher",add=True) # returns text

print(out)
# capture locally
out = get_files_and_dirs("/home/solcatcher", user_at_host="solcatcher",add=True) # returns text
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
