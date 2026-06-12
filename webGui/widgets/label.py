from webGui.html import tags

class Label(tags.Label):
    def __init__(self, text='', style=None, **kwargs):
        super().__init__(style=style, **kwargs)
        self.innerText(text)
        