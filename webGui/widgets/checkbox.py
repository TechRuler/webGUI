from webGui.html.tags import Div
from .label import Label
from .inputfield import CheckboxInput

class Checkbox(Div):
    def __init__(self, text="", value:bool=False, style=None, **kwargs):
        super().__init__(style=style, **kwargs)
        attrs = {}
        if value:
            attrs["checked"] = True

        self.checkboxinput = CheckboxInput(attrs=attrs)
        self.label = Label(text=text)
        self.label.set_attribute("for",f"{self.checkboxinput.id}")
        self.add(self.checkboxinput)
        self.add(self.label)

    