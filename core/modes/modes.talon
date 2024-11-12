not mode: sleep
-
^dictation mode$:
    user.dictation_mode()
^command (mode|made)$:
    user.command_mode()
^terminal mode$:
    user.terminal_mode()
^tab mode$:
    user.tab_mode()
