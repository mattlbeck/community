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