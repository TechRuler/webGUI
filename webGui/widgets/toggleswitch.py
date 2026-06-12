from webGui.html.tags import Span
from .label import Label
from .inputfield import CheckboxInput

class ToggleSwitch(Label):
    def __init__(self, value=False, style=None, **kwargs):
        super().__init__(style=style,**kwargs)

        switch = {
            "position": "relative",
            "display": "inline-block",
            "width": "60px",
            "height": "34px"
        }

        slider = {
            "position": "absolute",
            "inset": 0,
            "cursor": "pointer",
            "background": "#ccc",
            "border-radius": "34px",
            "transition": ".3s"
        }

        self.__apply_style(switch,self)

        self.input = CheckboxInput(
            attrs={"checked": value},
        )

        self.slider = Span(
            class_name="slider"
        )

        self.__apply_style(slider, self.slider)

        self.add(self.input)
        self.add(self.slider)

        
        

        self.input.hide()

        self.on('click', self.toggle)
        
    def toggle(self):
        checked = self.input.checked()

        self.input.checked(not checked)

        if not checked:
            self.slider.set_style("background", "#4CAF50")
            self.input.set_style("transform", "translateX(26px)")
        else:
            self.slider.set_style("background", "#ccc")
            self.input.set_style("transform", "translateX(0px)")
    def __apply_style(self, style, tag):
        for key, value in style.items():
            tag.set_style(key, value)