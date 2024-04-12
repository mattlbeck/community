from talon import Context, Module, actions, app

ctx = Context()
mod = Module()

mod.apps.zotero = "app.name: Zotero"
mod.apps.zotero = """
os: mac
app.bundle: com.zotero.Zotero
"""

ctx.matches = r"""
app: zotero
"""

@mod.action_class
class Actions:
    pass