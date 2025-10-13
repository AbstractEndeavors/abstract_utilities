from src.abstract_utilities.file_utils.file_utils.file_utils import *
directory = "/home/computron/Documents/pythonTools/modules/src/modules/abstract_ide/src/abstract_ide/consoles/apiTab/functions"

##out = get_files_and_dirs("/home/solcatcher",add=True) # returns text

dirs,files = get_files_and_dirs(directory=directory)
input(files)
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
