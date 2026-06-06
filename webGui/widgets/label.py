
import json
from webGui.widgets.base import BaseWidget

class Label(BaseWidget):
    def __init__(self, text="Static Text", class_name="", style=None, **kwargs):
        # Framework baseline design for layout text blocks
        default_style = {
            "fontSize": "16px", 
            "color": "#333333",
            "fontFamily": "inherit"
        }
        
        super().__init__(prefix="lbl", class_name=class_name, default_style=default_style, style=style, **kwargs)
        self.text = text
        
        
        # Safe merge: filters and converts user kebab-case strings to camelCase automatically
        # self.style = self.clean_style(style, kwargs, default_style)

    def render(self):
        window = self.get_window()
        if not window: return
        
        parent_target = getattr(self, '_target_parent_id', 'root')
        style_json = json.dumps(self.style)

        js_script = f"""
        (function() {{
            let lbl = document.createElement('span');
            lbl.id = '{self.id}';
            lbl.innerText = "{self.text}";
            Object.assign(lbl.style, {style_json});

            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                lbl.classList.add(...cls.trim().split(/\\s+/));
            }}
            
            // DYNAMIC PARENT TARGETING
            let targetNode = document.getElementById('{parent_target}');
            if (targetNode) {{
                targetNode.appendChild(lbl);
            }} else {{
                console.error("Framework Error: Target parent layout container element ID '{parent_target}' not found in DOM.");
            }}
        }})();
        """
        window.evaluate_js(js_script)

    def update_text(self, new_text):
        """Mutate text element in DOM live from Python execution pipeline"""
        self.text = new_text
        window = self.get_window()
        if window:
            window.evaluate_js(f"document.getElementById('{self.id}').innerText = '{new_text}';")
    