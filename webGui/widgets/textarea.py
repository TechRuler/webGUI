from webGui.html.tags import Textarea

class Text(Textarea):
    def __init__(self, attrs={}, children=[], style={}, **kwargs):
        super().__init__(attrs=attrs, children=children, style=style, **kwargs)
        