tag: user.markdown
-
heading <number_small> <user.text>:
    user.ensure_newline()
    insert('#'*number_small)
    insert(" ")
    user.insert_formatted(user.text, "title")
    edit.line_insert_down()


itemize:
    user.ensure_newline()
    insert(" - ")

enumerate:
    user.ensure_newline()
    insert("1. ")

item end:
    edit.line_insert_down()
    edit.line_insert_down()

link to [<user.text>]:
    user.dictation_insert("[[")
    insert(user.text or "")

    
link out:
    user.dictation_insert("[")

    edit.paste()
    user.dictation_insert("]")