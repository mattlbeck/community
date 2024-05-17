import re
from talon import Context, Module, actions, grammar, settings, ui
mod = Module()
ctx = Context()
max_tokens = 100

nav_map = {
    "word": (actions.edit.extend_word_left, actions.edit.extend_word_right),
    "line": (actions.edit.extend_line_up, actions.edit.extend_line_down),
    "char": (actions.edit.extend_left, actions.edit.extend_right),
}

        
def select_to(phrase: re.Pattern, forwards=True, token="word"):
    navigate = nav_map[token][int(forwards)]
    unnavigate = nav_map[token][int(not forwards)]
    
    navigate()
    text = actions.edit.selected_text()
    line_count = 0
    while not re.search(phrase, text.lower()):
        line_count += 1
        navigate()
        selected_text = actions.edit.selected_text()
        if selected_text == text or line_count > max_tokens:
            return
        text = selected_text
    return text
            

            
    
@mod.action_class
class Actions:
    def select_to(phrase: str):
        """select right until we hit a phrase"""
        
        phrase = re.escape(phrase.lower())


        text=select_to(re.compile(phrase), forwards=True, token="line")        
        if not text:
            return
            
        actions.edit.extend_line_up()    

        text = select_to(re.compile(phrase), forwards=True, token="word")
        if not text:
            return

    def select_back_to(phrase: str):
        """select left until we hit a phrase"""
        
        phrase = re.escape(phrase.lower())
        text=select_to(re.compile(phrase), forwards=False, token="line")        
        if not text:
            return
            
        actions.edit.extend_line_down()    

        text = select_to(re.compile(phrase), forwards=False, token="word")
        if not text:
            return
                
    def select_sentence():
        """select the entire sentence under the cursor"""
        text = select_to(r"\.\s", forwards=False, token="word")
        if text:
            actions.edit.left()
            actions.edit.right()
            actions.edit.right()
            actions.edit.right()
        else:
            actions.edit.right()
        text = select_to(r"\.\s", forwards=True, token="word")
        actions.edit.extend_left()

    def select_paragraph():
        """select the entire sentence under the cursor"""
        text = select_to(r"\n", forwards=False, token="line")
        if text:
            actions.edit.left()
            actions.edit.right()
        else:
            actions.edit.right()
        text = select_to(r"\n", forwards=True, token="line")
        actions.edit.extend_left()

    def select_chunk():
        """select the entire sentence under the cursor"""
        text = select_to(r"\s", forwards=False, token="char")
        if text:
            actions.edit.left()
            actions.edit.right()
        else:
            actions.edit.right()
        text = select_to(r"\s", forwards=True, token="char")
        actions.edit.extend_left()
            
        
