mode: command
mode: dictation
--
select to <user.text>$: user.select_to(user.text)
select back <user.text>$: user.select_back_to(user.text)
scrub to <user.text>$: 
    user.select_to(user.text)
    edit.right()
scrub back <user.text>$: 
    user.select_back_to(user.text)
    edit.left()
select sentence: user.select_sentence()
select paragraph: user.select_paragraph()
select chunk: user.select_chunk()