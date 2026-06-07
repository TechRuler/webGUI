import json
from webGui.widgets.base import BaseWidget

class Div(BaseWidget):
    def __init__(self, children=None, style=None, layout="block", **kwargs):
        self.children = children or []

        default_style = {
            "display": layout,   # block / flex / grid
            "boxSizing": "border-box"
        }

        super().__init__(
            prefix="div",
            default_style=default_style,
            style=style,
            **kwargs
        )

        

    def add(self, widget):
        widget._target_parent_id = self.id
        self.children.append(widget)
        return self

    def render(self):
        window = self.get_window()
        if not window:
            return

        parent_target = getattr(self, "_target_parent_id", "root")

        js = f"""
        (function(){{
            let div = document.createElement('div');
            div.id = '{self.id}';

            const cls = '{self.class_name}';
            if (cls && cls.trim()) {{
                div.classList.add(...cls.trim().split(/\\s+/));
            }}

            Object.assign(div.style, {json.dumps(self.style)});

            document.getElementById('{parent_target}').appendChild(div);
        }})();
        """

        window.evaluate_js(js)

        for child in self.children:
            child.app = self.app
            if hasattr(child, "render_inside"):
                child.render_inside(self.id)
            else:
                child._target_parent_id = self.id
                child.render()