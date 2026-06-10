import json
from webGui.core.base import BaseWidget
from webGui.config import state

class ContainerTag(BaseWidget):
    def __init__(self, tag="", attrs={}, children=None, class_name="", style=None, **kwargs):
        self.children = children or []

        

        super().__init__(
            prefix=tag,
            style=style,
            class_name=class_name,
            **kwargs
        )

        self.tag = tag
        self.attrs = attrs

    def add(self, widget):
        widget._target_parent_id = self.id
        self.children.append(widget)
        return self

    def render(self):
        window = self.get_window()
        if not window:
            return

        parent_target = getattr(self, "_target_parent_id", "root")

        attrs_js = ""

        if self.attrs:
            attrs_js = f"""
            const attrs = {json.dumps(self.attrs)};
            for (const [key, value] of Object.entries(attrs)) {{
                if (value !== null && value !== undefined) {{
                    element.setAttribute(key, value);
                }}
            }}
            """

        js = f"""
        (function(){{
            let element = document.createElement('{self.tag}');
            element.id = '{self.id}';

            const cls = '{json.dumps(self.class_name)}';
            if (cls && cls.trim()) {{
                element.classList.add(...cls.trim().split(/\\s+/));
            }}

            Object.assign(element.style, {json.dumps(self.style)});

            {attrs_js}

            document.getElementById('{parent_target}')
                .appendChild(element);
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
   
    