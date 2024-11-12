from talon import Context, Module
import subprocess

mod = Module()


@mod.action_class
class Actions:
    def terminal_list_directories():
        """Lists directories"""

    def terminal_list_all_directories():
        """Lists all directories including hidden"""

    def terminal_change_directory(path: str):
        """Lists change directory"""

    def terminal_change_directory_root():
        """Root of current drive"""

    def terminal_clear_screen():
        """Clear screen"""

    def terminal_run_last():
        """Repeats the last command"""

    def terminal_rerun_search(command: str):
        """Searches through the previously executed commands"""

    def terminal_kill_all():
        """kills the running command"""

def get_vaults():
    try:
        profiles = subprocess.check_output("aws-vault list --profiles", shell=True)
        return profiles.split("\n")
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        print(e.stdout)
        return []
    
ctx = Context()
ctx.lists["user.aws_vaults"] = get_vaults()