tag: user.tabs
mode: user.tab
-
(open | new): app.tab_open()
(last | previous): app.tab_previous()
next: app.tab_next()
close: user.tab_close_wrapper()
(reopen | restore): app.tab_reopen()
<number>: user.tab_jump(number)
final: user.tab_final()
duplicate: user.tab_duplicate()