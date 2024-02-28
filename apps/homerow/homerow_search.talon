mode: command
-
(pick | pic | get): user.homerow_pick("", false)
(pick | pic | get) <user.letters>: user.homerow_pick(letters, false)

(pick | pic | get) (and | end): user.homerow_pick("", true)
(pick | pic | get) <user.letters> (and | end): user.homerow_pick(letters, true)
