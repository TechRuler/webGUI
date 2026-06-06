# app/widgets/layout.py
import json
from app.widgets.base import BaseWidget

class Horizontal(BaseWidget):
    """A layout container that aligns its children horizontally using Flexbox."""
    def __init__(self, children=None, alignment="flex-start", gap="10px", style=None):
        # Initialize children from array if given, else leave empty for 'with' contexts
        self.children = children if children else []
        super().__init__(prefix="row")
        
        default_style = {
            "display": "flex",
            "flexDirection": "row",
            "justifyContent": alignment, # e.g., 'center', 'space-between'
            "alignItems": "center",
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

        # Read layout nesting target. Fallback to 'root' if top-level container
        parent_target = getattr(self, '_target_parent_id', 'root')

        # 1. Create the container element inside its proper parent element
        js_script = f"""
        (function() {{
            let rowDiv = document.createElement('div');
            rowDiv.id = '{self.id}';
            Object.assign(rowDiv.style, {json.dumps(self.style)});
            document.getElementById('{parent_target}').appendChild(rowDiv);
        }})();
        """
        window.evaluate_js(js_script)

        # 2. Tell the children to render themselves downstream
        for child in self.children:
            child.app = self.app # Pass app reference down
            
            # If the child widget has our custom render structure, use it, 
            # otherwise fall back to standard rendering
            if hasattr(child, 'render_inside'):
                child.render_inside(self.id)
            else:
                child._target_parent_id = self.id
                child.render()


class Vertical(BaseWidget):
    """A layout container that aligns its children vertically using Flexbox."""
    def __init__(self, children=None, alignment="flex-start", gap="10px", style=None):
        self.children = children if children else []
        super().__init__(prefix="col")
        
        default_style = {
            "display": "flex",
            "flexDirection": "column",
            "justifyContent": "flex-start",
            "alignItems": alignment, # e.g., 'center', 'stretch'
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
            let colDiv = document.createElement('div');
            colDiv.id = '{self.id}';
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