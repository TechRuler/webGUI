import json 
from webGui.core.base import BaseWidget

class TextArea(BaseWidget):
    def __init__(self, class_name="", style=None, **kwargs):
        super().__init__(prefix='textbox', class_name=class_name ,style=style, **kwargs)

    def render(self):
        window = self.get_window()
        if not window: return

        style_json = json.dumps(self.style)
        parent_target = getattr(self, '_target_parent_id', 'root')

        js_script = f"""
        (function() {{
            let ta = document.createElement('textarea');
            ta.id = '{self.id}';

            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                ta.classList.add(...cls.trim().split(/\\s+/));
            }}

            // placeholder support (optional)
            ta.placeholder = "{getattr(self, 'placeholder', '')}";

            // apply styles
            Object.assign(ta.style, {style_json});

            // basic UX styling (optional but useful)
            ta.style.resize = "none";
            ta.style.outline = "none";

            // DYNAMIC PARENT TARGETING
            let targetNode = document.getElementById('{parent_target}');
            if (targetNode) {{
                targetNode.appendChild(ta);
            }} else {{
                console.error("Framework Error: Parent '{parent_target}' not found.");
            }}

        }})();
        """
        window.evaluate_js(js_script)
    def set_value(self, value):
        window = self.get_window()
        if not window:
            return

        js = f"""
        document.getElementById('{self.id}').value = {json.dumps(value)};
        """
        window.evaluate_js(js)
    def get_value(self):
        try:
            window = self.get_window()
            if not window:
                raise Exception("No window")

            js = f"document.getElementById('{self.id}').value"
            result = window.evaluate_js(js)

            if result is None:
                raise Exception("DOM not ready")

            return result

        except:
            return self.get_info("value")
    def get_value_at(self, start, end):
        content:str = self.get_value()
        if end is None:
            return content[start]

        return content[start:end]
    
    def get_line(self, line_number: int):
        content: str = self.get_value() or ""
        lines = content.split("\n")

        if 0 <= line_number < len(lines):
            return lines[line_number]

        return ""
    
    def get_cursor_pos(self):
        window = self.get_window()
        if not window:
            return None

        js = f"""
        (function(){{
            const el = document.getElementById('{self.id}');
            if (!el) return null;

            return {{
                start: el.selectionStart,
                end: el.selectionEnd,
                hasSelection: el.selectionStart !== el.selectionEnd
            }};
        }})()
        """

        return window.evaluate_js(js)