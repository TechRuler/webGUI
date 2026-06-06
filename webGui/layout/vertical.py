import json
from webGui.widgets.base import BaseWidget


class VerticalDiv(BaseWidget):
    """A layout container that aligns its children vertically using Flexbox."""
    def __init__(self, children=None, alignment="flex-start", gap="10px", style=None, **kwargs):
        self.children = children if children else []
        default_style = {
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "flex-start",
            "alignItems": alignment, # e.g., 'center', 'stretch'
            "gap": gap,
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(prefix="col", default_style=default_style, style=style, **kwargs)


        # self.style = self.clean_style(style, kwargs, default_style)

        self.style["display"] = "flex" # Ensure flex display is always set
        self.style["flexDirection"] = "column" # Ensure column direction is always set
        self.style["justifyContent"] = self.style.get("justifyContent", "flex-start") # Ensure alignment is always set
        self.style["gap"] = self.style.get("gap", gap) # Ensure gap is always set

    def add(self, widget):
        """Allows users to manually append pre-declared widgets into this container."""
        widget._target_parent_id = self.id
        self.children.append(widget)
        return widget

    def render(self):
        window = self.get_window()
        if not window: return

        parent_target = getattr(self, '_target_parent_id', 'root')

        js_script = f"""
        (function() {{
            let colDiv = document.createElement('div');
            colDiv.id = '{self.id}';
            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                colDiv.classList.add(...cls.trim().split(/\\s+/));
            }}
            Object.assign(colDiv.style, {json.dumps(self.style)});
            document.getElementById('{parent_target}').appendChild(colDiv);
        }})();
        """
        window.evaluate_js(js_script)

        for child in self.children:
            child.app = self.app
            if hasattr(child, 'render_inside'):
                child.render_inside(self.id)
            else:
                child._target_parent_id = self.id
                child.render()
