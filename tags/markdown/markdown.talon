tag: user.markdown
-
heading <number_small> <user.text>:
    user.ensure_newline()
    insert('#'*number_small)
    insert(" ")
    user.insert_formatted(user.text, "title")
    edit.line_insert_down()


itemize:
    insert("- ")

enumerate:
    insert("1. ")

checkbox:
    insert("- [ ] ")

item end:
    edit.line_insert_down()
    sleep(50ms) 
    edit.line_insert_down()

link to [<user.text>]:
    user.dictation_insert("[[")
    insert(user.text or "")

    
link out:
    user.dictation_insert("[")

    edit.paste()
    user.dictation_insert("]")