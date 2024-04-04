from talon import Context, Module, actions, app, ui
import time

ctx = Context()
mod = Module()

mod.tag("homerow_search")


@ctx.action_class("user")
class UserActions:
    def homerow_search():
        actions.key("shift-ctrl-alt-h")
        ctx.tags = ["user.homerow_search"]
    
    def homerow_end():
        actions.key("escape")
        ctx.tags = []

    def homerow_click(letters: str, again: bool):
        actions.insert(letters.lower())
        actions.key("enter")
        if again:
            time.sleep(1)
            actions.key("shift-ctrl-alt-h")
        else:
            ctx.tags = []

    def homerow_righty():
        actions.key("shift-enter")
        ctx.tags = []

    def homerow_info():
        actions.key("?")

    def homerow_duke():
        actions.key("enter")
        actions.key("enter")
        ctx.tags = []


@mod.action_class
class Actions:
    def homerow_search():
        """Search in Homerow"""
    def homerow_end():
        """end Homerow search"""

    def homerow_click(letters: str, again: bool):
        """Click a home row item"""

    def homerow_righty():
        """Right click a home row item"""

    def homerow_duke():
        """Doubleclick a home row item"""

    def homerow_info():
        """Get info on an element"""