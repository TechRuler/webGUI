from webGui.html.tags import Div
from .label import Label
from .inputfield import RadioInput

class RadioButton(Div):
    def __init__(self, text='',group='default',style=None,**kwargs):
        super().__init__(
            style=style,
            **kwargs
        )
        self.radio = RadioInput(
            attrs={
                "name":group
            },
        )
        self.label = Label(text=text)
        self.label.set_attribute("for",f"{self.radio.id}")
        self.add(self.radio)
        self.add(self.label)