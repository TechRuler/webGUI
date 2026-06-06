
import webview 
from webGui.config import state, settings
from webGui.config.state import EVENT_REGISTRY

class App:
    def __init__(self, title="App", width=800, height=60):
        self.title = title
        self.components = []
        self.window = None
        self.width = width 
        self.height = height

        self._pending_js = []   # 🔥 add this
        
    def add(self, component):
        self.components.append(component)
        # Give the component a reference to the window so it can update itself later
        component.app = self
        return component

    # =====================================================================
    # LIVE ATTRIBUTE MUTATORS
    # =====================================================================
    def set_title(self, new_title):
        """Live mutate the application window title decoration bar."""
        self.title = new_title
        if self.window:
            self.window.set_title(new_title)

    def resize(self, new_width, new_height):
        """Live push canvas scaling geometry updates to the native engine frame."""
        self.width = new_width
        self.height = new_height
        if self.window:
            self.window.resize(new_width, new_height)

    def toggle_fullscreen(self):
        """Toggles windowed state directly between baseline layout size and fullscreen."""
        if self.window:
            self.window.toggle_fullscreen()

    def set_background(self, content):
        """Live mutate background (supports solid + gradients)."""

        js_script = f"""
        (function() {{
            document.body.style.background = "{content}";

            let rootNode = document.getElementById('root');
            if (rootNode) rootNode.style.background = "{content}";
        }})();
        """

        if self.window:
            self.window.evaluate_js(js_script)
        else:
            self._pending_js.append(js_script)

    # =====================================================================
    # LIFECYCLE MANAGEMENT
    # =====================================================================
    def run(self):
        # The base HTML is just an empty canvas with pywebview's API bridge ready
        base_html = settings.BASE_HTML
        
        # Create the JS API bridge so frontend clicks can talk to Python functions
        class JSBridge:
            def trigger_event(self, event_id, data=None):
                """A universal event handler for every single widget."""
                if event_id in EVENT_REGISTRY:
                    # If the widget sent data (like text or a slider value), pass it to Python
                    if data is not None:
                        EVENT_REGISTRY[event_id](data)
                    else:
                        EVENT_REGISTRY[event_id]() # Standard click with no data

        self.window = webview.create_window(
            title=self.title,
            width=self.width,
            height=self.height, 
            html=base_html, 
            js_api=JSBridge()
        )
        
        # FIX: Explicitly mutate the imported shared config state module
        state.ACTIVE_WINDOW = self.window
        
        # Once the window loads, render all components that the user added
        webview.start(self._on_loaded)
    
    def _on_loaded(self):
        self._initial_render()

    def _initial_render(self):
        for comp in self.components:
            comp.app = self  # Ensure cascading reference matching
            comp.render()
        
        # 🔥 execute queued JS
        for js in self._pending_js:
            self.window.evaluate_js(js)

        self._pending_js.clear()