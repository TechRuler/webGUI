from webGui.widgets.base import BaseWidget
import json 

class InputField(BaseWidget):
    def __init__(self, placeholder="", value="", on_change=None, style=None, **kwargs):
        default_style = {
            "width":"max-width"
        }
        super().__init__(prefix="input", on_event=on_change, event_suffix="change", style=style, default_style=default_style, **kwargs)
        self.placeholder = placeholder
        self.value = value
        

    def render(self):
        window = self.get_window()
        if not window: return

        style_json = json.dumps(self.style)
        parent_target = getattr(self, '_target_parent_id', 'root')

        js_script = f"""
        (function(){{
            let input = document.createElement('input');
            input.id = '{self.id}';

            const cls = '{self.class_name}';

            if (cls && cls.trim()){{
                input.classList.add(...cls.trim().split(/\\s+/));
            }}

            input.type = 'text';
            input.value = '{self.value}';
            input.placeholder = '{self.placeholder}'
            Object.assign(input.style, {style_json});

            let targetNode = document.getElementById('{parent_target}');
            if (targetNode) {{
                targetNode.appendChild(input);
            }} else {{
                console.error("Framework Error: Target parent layout container element ID '{parent_target}' not found in DOM.");
            }}
            
        }})();
        """

        window.evaluate_js(js_script)
    
