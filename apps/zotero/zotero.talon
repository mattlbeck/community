:os: mac
app: zotero
-
tag(): user.tabs

(pain| pane) items: key("cmd-ctrl-shift-i")
(pain| pane) collections: key("cmd-ctrl-shift-c")
spread odd:
    key("ctrl-f2")
    sleep(50ms)
    key("v")
    sleep(50ms)
    key("enter")
    sleep(50ms)
    key("o")
    sleep(50ms)
    key("enter")