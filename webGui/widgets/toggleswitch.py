from webGui.html.tags import Span
from .label import Label
from .inputfield import CheckboxInput


class ToggleSwitch(Label):
    def __init__(self, value=False, style=None, **kwargs):
        kwargs["default_style"] = {
            "position": "relative",
            "display": "inline-block",
            "width": "60px",
            "height": "34px",
            "cursor": "pointer"
        }
        super().__init__(style=style, **kwargs)

        self.active_color = "#4CAF50"
        self.bgcolor = "#ccc"

        self.input = CheckboxInput(
            attrs={"checked": value}
        )

        self.slider = Span(default_style = {
            "position": "absolute",
            "inset": "0",
            "background": self.bgcolor,
            "border-radius": "34px",
            "transition": "0.3s"
        })

        self.knob = Span(default_style = {
            "position": "absolute",
            "width": "26px",
            "height": "26px",
            "left": "4px",
            "bottom": "4px",
            "background": "white",
            "border-radius": "50%",
            "transition": "0.3s",
            "box-shadow": "0 1px 3px rgba(0,0,0,0.3)"
        })

        self.slider.add(self.knob)
        self.input.checked(False)

        self.add(self.input)
        self.add(self.slider)

        self.input.hide()

        if value:
            self.slider.set_style("background", self.active_color)
            self.knob.set_style("transform", "translateX(26px)")

        self.on("click", self.toggle)
    
    def slider_bgcolor(self, color):
        self.slider.set_style("background",color)
        self.bgcolor = color
    
    def active(self, color):
        self.active_color = color
        

    def toggle(self):
        checked = self.input.checked()
        
        if checked:
            self.slider.set_style("background", self.active_color)
            self.knob.set_style("transform", "translateX(26px)")
        else:
            
            self.slider.set_style("background", self.bgcolor)
            self.knob.set_style("transform", "translateX(0px)")

    def is_checked(self):
        return self.input.checked()

    def set_checked(self, value: bool):
        self.input.checked(value)

        if value:
            self.slider.set_style("background", self.active_color)
            self.knob.set_style("transform", "translateX(26px)")
        else:
            self.slider.set_style("background", self.bgcolor)
            self.knob.set_style("transform", "translateX(0px)")