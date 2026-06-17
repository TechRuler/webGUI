from webGui.html.tags import Div

class Frame(Div):
    def __init__(self, children=None, class_name=None, style=None, **kwargs):
        super().__init__(style=style, class_name=class_name, children=children, **kwargs)

class Grid(Frame):
     def __init__(self, children=None, columns="repeat(3, 1fr)", style=None, **kwargs):
        children = children if children else []
        kwargs["default_style"] = {
            "display": "grid",
            "gridTemplateColumns": columns, # e.g., 'repeat(3, 1fr)' or '200px 1fr'
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(children=children, style=style, **kwargs)
        
        # default_style = {
        #     "display": "grid",
        #     "gridTemplateColumns": columns, # e.g., 'repeat(3, 1fr)' or '200px 1fr'
        #     "width": "100%",
        #     "boxSizing": "border-box"
        # }
        # for key, value in default_style.items():
        #     self.set_style(key, value)

class HorizontalFrame(Frame):
    def __init__(self, children=None, alignment="flex-start", class_name="", style=None, **kwargs):
        children = children if children else []
        kwargs["default_style"] = {
            "display": "flex",
            "flexDirection": "row",
            "justifyContent": alignment, 
            "alignItems": "center",
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(children=children, class_name=class_name, style=style, **kwargs)

        # default_style = {
        #     "display": "flex",
        #     "flexDirection": "row",
        #     "justifyContent": alignment, 
        #     "alignItems": "center",
        #     "width": "100%",
        #     "boxSizing": "border-box"
        # }
        # for key, value in default_style.items():
        #     self.set_style(key, value)
class VerticalFrame(Frame):
    def __init__(self, children=None, alignment="flex-start",class_name=None, style=None, **kwargs):
        children = children if children else []
        kwargs["default_style"] = default_style = {
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "flex-start",
            "alignItems": alignment, 
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(children=children, class_name=class_name, style=style, **kwargs)
        # default_style = {
        #     "display": "flex",
        #     "flexDirection": "column",
        #     "justifyContent": "flex-start",
        #     "alignItems": alignment, 
        #     "width": "100%",
        #     "boxSizing": "border-box"
        # }
        # for key, value in default_style.items():
        #     self.set_style(key, value)

