app: obsidian
-
tag(): user.markdown
tag(): user.tabs

please [<user.text>]:
    key("cmd-p")
    sleep(50ms)
    insert(user.text or "")

note create [<user.text>]:
    key("cmd-n")
    sleep(50ms)
    user.insert_formatted(user.text or "" , "title")
    user.ensure_newline()

note hunt <user.text>:
    key("cmd-o")
    sleep(50ms)
    insert(user.text)

paper hunt <user.text>:
    key("cmd-o")
    sleep(50ms)
    insert("papers/")
    insert(user.text)

go line <number_small>:
    key("ctrl-g")
    sleep(50ms)
    insert(number_small)
    key("enter")

paper add:
    key("cmd-p")
    sleep(50ms)
    insert("zotero create")
    key("enter")

