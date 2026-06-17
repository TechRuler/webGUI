from webGui.html.tags import Div 

class ListBox(Div):
    def __init__(self, class_name=None, style=None, **kwargs):
        kwargs["default_style"] = {
            "border":"1px solid black"
        }
        super().__init__(class_name=class_name, style=style, **kwargs)
        self.items = []
        
    def add_item(self, item):
        it = Div()
        it.innerText(item)
        self.add(it)
        self.items.append(it)