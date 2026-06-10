import json
from webGui.core.base import BaseWidget


class GridDiv(BaseWidget):
    """A highly dynamic layout container using CSS Grid."""
    def __init__(self, children=None, columns="repeat(3, 1fr)", gap="15px", style=None, **kwargs):
        self.children = children if children else []
        default_style = {
            "display": "grid",
            "gridTemplateColumns": columns, # e.g., 'repeat(3, 1fr)' or '200px 1fr'
            "gap": gap,
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(prefix="grid", default_style=default_style, style=style, **kwargs)


        # self.style = self.clean_style(style, kwargs, default_style)

        self.style["display"] = "grid" # Ensure grid display is always set
        self.style["gridTemplateColumns"] = self.style.get("gridTemplateColumns", columns) # Ensure columns are always set
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
            let gridDiv = document.createElement('div');
            gridDiv.id = '{self.id}';
            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                gridDiv.classList.add(...cls.trim().split(/\\s+/));
            }}
            Object.assign(gridDiv.style, {json.dumps(self.style)});
            document.getElementById('{parent_target}').appendChild(gridDiv);
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