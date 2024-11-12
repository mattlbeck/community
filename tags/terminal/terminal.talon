tag: terminal
-
# tags should be activated for each specific terminal in the respective talon file

lisa: user.terminal_list_directories()
lisa all: user.terminal_list_all_directories()
katie [dir] [<user.text>]: user.terminal_change_directory(text or "")
katie root: user.terminal_change_directory_root()
katie (up | back): user.terminal_change_directory("..")
go <user.system_path>: insert('cd "{system_path}"\n')
path <user.system_path>: insert('"{system_path}"')
clear screen: user.terminal_clear_screen()
run last: user.terminal_run_last()
rerun [<user.text>]: user.terminal_rerun_search(text or "")
rerun search: user.terminal_rerun_search("")
kill all: user.terminal_kill_all()

copy paste:
    edit.copy()
    sleep(50ms)
    edit.paste()

(clear | junk) word left: key("alt-backspace")
(clear | junk) word right: key("alt-delete")
go word left: key("alt-left")
go word right: key("alt-right")

exit: 
    insert("exit")
    key("enter")

ors activate <user.text>: 
    insert("aws-vault exec {text} --no-session")
    key("enter")

# command building helpers
long flag <user.text>: insert("--{text}")
short flag <user.letter>: insert("-{letter}")

history <user.text>: 
    key("ctrl-r")
    insert(user.text)
history$: 
    key("ctrl-r")