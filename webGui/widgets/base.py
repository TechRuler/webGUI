
import uuid
from webGui.config import state

class BaseWidget:
    def __init__(self, prefix="widget", on_event=None, event_suffix="action", className=""):
        # 1. Automatically generate a clean, unique ID for every single widget
        self.id = f"{prefix}_{uuid.uuid4().hex[:8]}"
        self.app = None
        self.className = className
        
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
            state.EVENT_REGISTRY[event_key] = on_event

    def get_window(self):
        """Helper to safely fetch the active window from context or parent app."""
        if self.app and self.app.window:
            return self.app.window
        if hasattr(state, 'ACTIVE_WINDOW') and state.ACTIVE_WINDOW:
            return state.ACTIVE_WINDOW
        return None

    def update_style(self, property_name, value):
        """A universal method allowing users to change ANY CSS property on the fly!"""
        window = self.get_window()
        if window:
            # e.g., document.getElementById('btn_123').style.backgroundColor = 'red';
            js_update = f"document.getElementById('{self.id}').style.{property_name} = '{value}';"
            window.evaluate_js(js_update)

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
        return self.className
    
    def get_id(self):
        return self.id

    # 4. CONTEXT SCOPE HOOKS (Enables the 'with' statement for containers)
    def __enter__(self):
        if not hasattr(state, 'LAYOUT_STACK'):
            state.LAYOUT_STACK = []
        state.LAYOUT_STACK.append(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if hasattr(state, 'LAYOUT_STACK') and state.LAYOUT_STACK:
            state.LAYOUT_STACK.pop()