
import json
from webGui.core.base import BaseWidget

class Button(BaseWidget):
    def __init__(self, text="Button", bg_color=None, on_click=None, class_name="", style=None, **kwargs):
        # Pass prefix and event type to the base class
        button_bg = bg_color if bg_color else "#3498db"

        # Default button layout styles
        default_style = {
            # "backgroundColor": button_bg,
            # "color": "white",
            # "padding": "10px 20px",
            # "border": "none",
            # "borderRadius": "6px",
            # "cursor": "pointer",
            # "width": "max-content", 
            # "fontSize": "16px",
            # "transition": "filter 0.2s" # Enables smooth brightness transitions on hover
        }
        super().__init__(
            prefix="btn",
            on_event=on_click, 
            event_suffix="click", 
            class_name=class_name,
            default_style=default_style,
            style=style,
            **kwargs)
        self.text = text

        # Fallback to framework default color if bg_color is omitted
        
        
        # Safe merge: converts user kebab-case strings to camelCase automatically
        # self.style = self.clean_style(style, kwargs, default_style)
       
    def render(self):
        window = self.get_window()
        if not window: return

        style_json = json.dumps(self.style)
        parent_target = getattr(self, '_target_parent_id', 'root')

        js_script = f"""
        (function() {{
            let btn = document.createElement('button');
            btn.id = '{self.id}';

            const cls = '{self.class_name}';

            if (cls && cls.trim()) {{
                btn.classList.add(...cls.trim().split(/\\s+/));
            }}

            btn.innerText = "{self.text}";
            Object.assign(btn.style, {style_json});

            // FIX: Changed Python '#' comment to a valid JavaScript '//' comment 👇
            btn.onmouseover = () => btn.style.filter = "brightness(0.9)";
            btn.onmouseout = () => btn.style.filter = "brightness(1)";

            btn.onclick = () => {{
                window.pywebview.api.trigger('{self.id}_click');
            }};

            // DYNAMIC PARENT TARGETING
            let targetNode = document.getElementById('{parent_target}');
            if (targetNode) {{
                targetNode.appendChild(btn);
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