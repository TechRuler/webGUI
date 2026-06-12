import uuid
from webGui.config import state
from .dom_mixin import DOMMixin
from .event_mixin import EventMixin
from .style_mixin import StyleMixin

class BaseWidget(
    DOMMixin,
    EventMixin,
    StyleMixin
):
    def __init__(self, prefix="widget", on_event=None, event_suffix="action", class_name="", style=None, default_style=None, **kwargs):
        # Automatically generate a clean, unique ID for every single widget
        self.id = f"{prefix}_{uuid.uuid4().hex[:8]}"
        self.app = None
        self.class_name = class_name
        self._rendered = False
        self._pending_ops = []

        self.style = self.clean_style(style, kwargs, default_style)
        
        # Default target parent is the main canvas root
        self._target_parent_id = "root"
        
        # CONTEXT MANAGEMENT: Auto-detect if inside a layout 'with' block
        if hasattr(state, 'LAYOUT_STACK') and state.LAYOUT_STACK:
            active_container = state.LAYOUT_STACK[-1]
            self._target_parent_id = active_container.id
            active_container.children.append(self)

        # Automatically handle event registration for any widget type
        if on_event:
            event_key = f"{self.id}_{event_suffix}"
           
            state.EVENT_HANDLERS[event_key] = on_event
            

    
    
    def get_window(self):
        """Helper to safely fetch the active window from context or parent app."""
        if self.app and self.app.window:
            return self.app.window
        if hasattr(state, 'ACTIVE_WINDOW') and state.ACTIVE_WINDOW:
            return state.ACTIVE_WINDOW
        return None

    def _execute_js(self, js):
        window = self.get_window()

        if window:
            return window.evaluate_js(js)

        state._PENDING_JS.append(js)
        return None
    
    def _run_dom_js(self, js):
        if not self._rendered:
            self._pending_ops.append(js)
            return None

        return self._execute_js(js)

    def _mark_rendered(self):
        self._rendered = True

        if self._pending_ops:
            for js in self._pending_ops:
                self._execute_js(js)

            self._pending_ops.clear()

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
    
    


    
        
    # CONTEXT SCOPE HOOKS (Enables the 'with' statement for containers)
    def __enter__(self):
        if not hasattr(state, 'LAYOUT_STACK'):
            state.LAYOUT_STACK = []
        state.LAYOUT_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(state, 'LAYOUT_STACK') and state.LAYOUT_STACK:
            state.LAYOUT_STACK.pop()