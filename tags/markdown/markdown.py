from talon import Context, Module, actions, app
ctx = Context()
ctx.matches = r"""
tag: markdown
"""

mod = Module()
mod.tag("markdown", desc="commands for writing markdown")

@mod.action_class
class UserActions:
    def ensure_newline():
        """insert a new line if the current line is not empty"""
        before, after = actions.user.dictation_peek(left=True, right=False)
        if before:
            actions.edit.line_insert_down()

        