
import uuid
from webGui.config import state
import json

class BaseWidget:
    def __init__(self, prefix="widget", on_event=None, event_suffix="action", class_name="", style=None, default_style=None, **kwargs):
        # 1. Automatically generate a clean, unique ID for every single widget
        self.id = f"{prefix}_{uuid.uuid4().hex[:8]}"
        self.app = None
        self.class_name = class_name

        self.style = self.clean_style(style, kwargs, default_style)
        
        # Default target parent is the main canvas root
        self._target_parent_id = "root"
        
        # 2. CONTEXT MANAGEMENT: Auto-detect if inside a layout 'with' block
        if hasattr(state, 'LAYOUT_STACK') and state.LAYOUT_STACK:
            active_container = state.LAYOUT_STACK[-1]
            self._target_parent_id = active_container.id
            active_container.children.append(self)

        # 3. Automatically handle event registration for any widget type
        if on_event:
            event_key = f"{self.id}_{event_suffix}"
            # state.EVENT_REGISTRY[event_key] = {
            #     'data':{},
            #     'callback':on_event
            # }
            state.EVENT_HANDLERS[event_key] = on_event
            # state.EVENT_DATA[event_key] = {}

    def get_window(self):
        """Helper to safely fetch the active window from context or parent app."""
        if self.app and self.app.window:
            return self.app.window
        if hasattr(state, 'ACTIVE_WINDOW') and state.ACTIVE_WINDOW:
            return state.ACTIVE_WINDOW
        return None

    def update_style(self, property_name, value):
        """A universal method allowing users to change ANY CSS property on the fly!"""
        self.style[property_name] = value
        window = self.get_window()
        if window:
            # e.g., document.getElementById('btn_123').style.backgroundColor = 'red';
            js_update = f"document.getElementById('{self.id}').style.{property_name} = '{value}';"
            window.evaluate_js(js_update)
            
    
    def get_config(self, property_name):
        """
        Safe getter for:
        - public props (text, class_name, etc.)
        - style props (backgroundColor, padding, etc.)
        """

        # 1. SAFE whitelist of direct props
        direct_props = {
            "id": self.id,
            "class_name": self.class_name,
        }

        if property_name in direct_props:
            return direct_props[property_name]

        # 2. widget-defined attributes (SAFE ONLY)
        if hasattr(self, property_name) and not property_name.startswith("_"):
            return getattr(self, property_name)

        # 3. style lookup
        if hasattr(self, "style") and property_name in self.style:
            return self.style[property_name]

        
        return None

    def render_inside(self, parent_id):
        """
        Interceptors rule! If a widget is placed inside a layout container, 
        we temporarily override its render behavior to target that container's ID.
        """
        # Save original render method, swap the targeting logic, run it, restore it.
        self._target_parent_id = parent_id
        if hasattr(self, 'render'):
            self.render()
        self._target_parent_id = "root" # Reset fallback
    
    def get_class_name(self):
        return self.class_name
    
    def get_id(self):
        return self.id
    
    def _normalize_styles(self, style):
        if not style:
            return {}

        result = {}
        for k, v in style.items():
            parts = k.split("-")
            camel = parts[0] + "".join(p.title() for p in parts[1:])
            result[camel] = v
        return result
    
    def _snake_to_camel(self, kwargs):
        if not kwargs:
                return {}
        
        result = {}

        for k, v in kwargs.items():
            parts = k.split("_")
            camel = parts[0] + "".join(p.title() for p in parts[1:])
            result[camel] = v
        return result
    
    def clean_style(self, style, kwargs, default_style=None):
        style = self._normalize_styles(style or {})
        kwargs_style = self._snake_to_camel(kwargs or {})

        # merge both correctly
        override = {**style, **kwargs_style}

        if default_style is None:
            default_style = {}
        result = {**default_style, **override}


        return result
    
    def register_event(self, event_type):
        js = f"""
        (function() {{
            let el = document.getElementById({json.dumps(self.id)});
            if (!el) return;

            el.addEventListener({json.dumps(event_type)}, () => {{
                if (window.pywebview?.api?.trigger) {{
                    window.pywebview.api.trigger(
                        {json.dumps(f"{self.id}_{event_type}")}
                    );
                }}
            }});
        }})();
        """

        state._PENDING_JS.append(js)
    
    def addEventListener(self, event_type, callback):
        event_key = f"{self.id}_{event_type}"

        
        state.EVENT_HANDLERS[event_key] = callback

        # ONLY bind JS once
        self.register_event(event_type)

        return self
    on = addEventListener # Alias for more intuitive syntax

    def get_info_from_js(self, event_id, req_id):
        window = self.get_window()
        if not window:
            return

        js = f"""
        (function(){{
            const el = document.getElementById('{self.id}');
            if (!el) return;

            const cs = window.getComputedStyle(el);
            const style = {{}};

            for (let i = 0; i < cs.length; i++) {{
                const p = cs[i];
                const v = cs.getPropertyValue(p);
                if (v) style[p] = v;
            }}

            const data = {{
                req_id: "{req_id}",
                tag: el.tagName.toLowerCase(),
                value: ("value" in el) ? el.value : null,
                class: Array.from(el.classList),
                text: el.innerText,
                html: el.innerHTML,
                style: style
            }};

            window.pywebview.api.trigger('{event_id}', null, data);
        }})();
        """

        window.evaluate_js(js)

    # =========================================================
    # GET INFO (SYNC WRAPPER OVER ASYNC BRIDGE)
    # =========================================================
    def get_info(self, prop):
        req_id = uuid.uuid4().hex
        event_id = f"{self.id}_get"

        state._FUTURES[req_id] = {
            "done": False,
            "value": None
        }

        self.get_info_from_js(event_id, req_id)

        # wait loop
        for _ in range(50):
            future = state._FUTURES.get(req_id)

            if future and future["done"]:
                data = future["value"]
                if not data:
                    return None

                if prop in data:
                    return data[prop]

                if "style" in data and prop in data["style"]:
                    return data["style"][prop]

        return self.get_config(prop)

    # 4. CONTEXT SCOPE HOOKS (Enables the 'with' statement for containers)
    def __enter__(self):
        if not hasattr(state, 'LAYOUT_STACK'):
            state.LAYOUT_STACK = []
        state.LAYOUT_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(state, 'LAYOUT_STACK') and state.LAYOUT_STACK:
            state.LAYOUT_STACK.pop()