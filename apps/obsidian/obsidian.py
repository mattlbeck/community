from talon import Context, Module, actions, app, ui
mod = Module()
mod.apps.obsidian = """
os: mac
app.bundle: md.obsidian
"""
@mod.action_class
class Actions:
    def obsidian_open():
        """focus the obsidian app"""
        obsidian = get_app("Obsidian")
        actions.user.switcher_focus_app(obsidian)



def get_app(app_name) -> ui.App:

    for app in ui.apps():
        if app.name == app_name:
            return app

    raise RuntimeError("app could not be found")
        