from talon import Module, actions, app, speech_system

mod = Module()

modes = {
    "debug": "a way to force debugger commands to be loaded",
    "ida": "a way to force ida commands to be loaded",
    "presentation": "a more strict form of sleep where only a more strict wake up command works",
    "terminal": 'For manual activation of commands for terminal',
}

for key, value in modes.items():
    mod.mode(key, value)


@mod.action_class
class Actions:
    def talon_mode():
        """For windows and Mac with Dragon, enables Talon commands and Dragon's command mode."""
        actions.speech.enable()

        engine = speech_system.engine.name
        # app.notify(engine)
        if "dragon" in engine:
            if app.platform == "mac":
                actions.user.engine_sleep()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("switch to command mode")

    def dragon_mode():
        """For windows and Mac with Dragon, disables Talon commands and exits Dragon's command mode"""
        engine = speech_system.engine.name
        # app.notify(engine)

        if "dragon" in engine:
            # app.notify("dragon mode")
            actions.speech.disable()
            if app.platform == "mac":
                actions.user.engine_wake()
            elif app.platform == "windows":
                actions.user.engine_wake()
                # note: this may not do anything for all versions of Dragon. Requires Pro.
                actions.user.engine_mimic("start normal mode")
    
    def dictation_mode():
        """Enable dictation mode"""
        actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.enable("dictation")
        actions.user.code_clear_language_mode()
        actions.user.gdb_disable()
        actions.mode.disable("user.terminal")

    def command_mode():
        """Enable command mode"""
        actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")
        actions.mode.disable("user.terminal")

    def terminal_mode():
        """Enable terminal mode"""
        
        actions.mode.disable("sleep")
        actions.mode.disable("command")
        actions.mode.disable("dictation")
        actions.mode.enable("user.terminal")
            
        
