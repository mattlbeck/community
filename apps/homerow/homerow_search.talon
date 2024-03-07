mode: command
tag: user.homerow_search
-
(pick | pic | get): user.homerow_click("", true)
(pick | pic | get) <user.letters>: user.homerow_click(letters, true)

(pick | pic | get) (and | end): user.homerow_click("", false)
(pick | pic | get) <user.letters> (and | end): user.homerow_click(letters, false)
