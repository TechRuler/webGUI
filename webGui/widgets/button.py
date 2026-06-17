from webGui.html.tags import Button as button
from webGui.config import state

class Button(button):
    def __init__(self, text='', on_click=None, style=None, **kwargs):

        super().__init__(style=style, **kwargs)
        if on_click:
            event_key = f"{self.id}_click"
            state.EVENT_HANDLERS[event_key] = on_click
            self.on('click', on_click)
        self.innerText(text)
    
   