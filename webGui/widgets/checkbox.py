from webGui.widgets.base import BaseWidget
import json
from webGui.config import state

class CheckBox(BaseWidget):
    def __init__(self, text="Checkbox", checked=False, on_toggle=None, class_name="", style=None, **kwargs):
        # Pass style as-is without packing heavy default dicts!
        super().__init__(
            prefix='checkbox', 
            on_event=on_toggle, 
            event_suffix='toggle', 
            class_name=class_name, 
            style=style, 
            **kwargs
        )
        self.text = text
        self.checked = checked

    def render(self):
        window = self.get_window()
        if not window:
            return

        style_json = json.dumps(self.style)
        parent_target = getattr(self, '_target_parent_id', 'root')

        # safe text escaping (important for JS injection safety)
        safe_text = self.text.replace('"', '\\"').replace("\n", "\\n")

        js_script = f"""
        (function(){{
            const div = document.createElement('div');
            div.id = '{self.id}';

            const input = document.createElement('input');
            input.type = 'checkbox';
            input.checked = {str(self.checked).lower()};
            input.id = "{self.id}_checkbox";

            const label = document.createElement('label');
            label.innerText = "{safe_text}";
            label.htmlFor = input.id;
            label.id = "{self.id}_label";

           
            Object.assign(div.style, {style_json});

            

            

            div.appendChild(input);
            div.appendChild(label);

            // PARENT ATTACHMENT
            let targetNode = document.getElementById('{parent_target}');
            if (targetNode) {{
                targetNode.appendChild(div);
            }} else {{
                console.error("Framework Error: Target parent '{parent_target}' not found.");
            }}
        }})();
        """

        window.evaluate_js(js_script)
        
    def label_style(self, style=None, **kwargs):
        window = self.get_window()

        style = self.clean_style(style, kwargs)
        style_json = json.dumps(style)

        js_script = f"""
        (function(){{
            const label = document.getElementById('{self.id}_label');

            if (!label) {{
                console.error("label not found: {self.id}_label");
                return;
            }}

            Object.assign(label.style, {style_json});
        }})();
        """

        if window:
            window.evaluate_js(js_script)
        else:
            state._PENDING_JS.append(js_script)
    
    
    def box_style(self, style=None, **kwargs):
        window = self.get_window()

        style = self.clean_style(style, kwargs)
        style_json = json.dumps(style)

        js_script = f"""
        (function(){{
            const box = document.getElementById('{self.id}_checkbox');

            if (!box) {{
                console.error("checkbox not found: {self.id}_checkbox");
                return;
            }}

            Object.assign(box.style, {style_json});
        }})();
        """

        if window:
            window.evaluate_js(js_script)
        else:
            state._PENDING_JS.append(js_script)
    
    def get_value(self):
        window = self.get_window()
        if window:
            return window.evaluate_js(f"""
            (function () {{
                const checkbox = document.getElementById('{self.id}_checkbox');
                if (!checkbox) return false;
                return checkbox.checked;
            }})()
            """)
    def set_value(self, value:bool):
        window = self.get_window()
        if window:
            window.evaluate_js(f"""
            (function () {{
                const checkbox = document.getElementById('{self.id}_checkbox');
                
                checkbox.checked = '{value}';
            }})()
            """)
    def update_style_box(self, property_name, value):
        self.update_style(property_name, value, f"{self.id}_checkbox")

    def update_style_label(self, property_name, value):
        self.update_style(property_name, value, f"{self.id}_label")
    