import json
from app.widgets.base import BaseWidget


class Grid(BaseWidget):
    """A highly dynamic layout container using CSS Grid."""
    def __init__(self, children=None, columns="repeat(3, 1fr)", gap="15px", style=None):
        self.children = children if children else []
        super().__init__(prefix="grid")
        
        default_style = {
            "display": "grid",
            "gridTemplateColumns": columns, # e.g., 'repeat(3, 1fr)' or '200px 1fr'
            "gap": gap,
            "width": "100%",
            "boxSizing": "border-box"
        }
        self.style = {**default_style, **(style or {})}

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