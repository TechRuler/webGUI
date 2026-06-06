import json
from webGui.widgets.base import BaseWidget

class HorizontalDiv(BaseWidget):
    """A layout container that aligns its children horizontally using Flexbox."""
    def __init__(self, children=None, alignment="flex-start", gap="10px", class_name="", style=None, **kwargs):
        # Initialize children from array if given, else leave empty for 'with' contexts
        self.children = children if children else []
        default_style = {
            "display": "flex",
            "flexDirection": "row",
            "justifyContent": alignment, # e.g., 'center', 'space-between'
            "alignItems": "center",
            "gap": gap,
            "width": "100%",
            "boxSizing": "border-box"
        }
        super().__init__(prefix="row", class_name=class_name, default_style=default_style, style=style, **kwargs)

        # self.style = self.clean_style(style, kwargs, default_style)

        self.style["display"] = "flex" # Ensure flex display is always set
        self.style["flexDirection"] = "row" # Ensure row direction is always set
        self.style["justifyContent"] = self.style.get("justifyContent", alignment) # Ensure alignment is always set
        self.style["gap"] = self.style.get("gap", gap) # Ensure gap is always set

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
            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                rowDiv.classList.add(...cls.trim().split(/\\s+/));
            }}
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

