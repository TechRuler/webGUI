
import webview, time
from webGui.config import state, settings
import json
import os

class App:
    def __init__(self, title="App", width=800, height=60):
        self.title = title
        self.components = []
        self.window = None
        self.width = width 
        self.height = height
    
    def load_style(self, path: str):
        """
        Parses external .css or .json files and instantly routes them 
        to the appropriate internal injection pipeline.
        """
        if not isinstance(path, str):
            return 
            
        if not os.path.exists(path):
            print(f"[Error]: File not found at {path}")
            return

        if path.endswith(".css"):
            with open(path, 'r', encoding='utf-8') as f:
                css_content = f.read()
            # Pass raw string data to the style sheet injector
            self._apply_css_stylesheet(css_content)
            
        elif path.endswith(".json"):
            with open(path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            # Pass dictionary to global style mapping tool
            self._apply_json_theme(json_data)
            
        else:
            print(f'[Error]: {path} format not supported. Only .json or .css files are allowed.')

    def _apply_css_stylesheet(self, content: str):
        """Injects a global CSS style sheet directly into the document header."""
        # Clean up line breaks and escape backticks for safe JS execution
        safe_content = content.replace("`", "\\`").replace("\r", "")
        
        js_script = f"""
        (function() {{
            let themeStyle = document.getElementById('global_framework_stylesheet');
            if (!themeStyle) {{
                themeStyle = document.createElement('style');
                themeStyle.id = 'global_framework_stylesheet';
                document.head.appendChild(themeStyle);
            }}
            themeStyle.innerHTML += `{safe_content}`;
        }})();
        """
        
        # Safe lifecycle execution routing
        if self.window:
            self.window.evaluate_js(js_script)
        else:
            from webGui.config import state
            state._PENDING_JS.append(js_script)

    def _apply_json_theme(self, theme_dict: dict):
        """
        Maps global JSON style tokens onto matching component class selectors 
        or saves them into a framework styling lookup state.
        """
        # Option A: Save it as a structural design blueprint variable on your app
        self.theme_tokens = theme_dict
        
        # Option B: If the JSON contains target classes (e.g., {"entry": {"backgroundColor": "red"}}),
        # you can iterate through existing pre-rendered component arrays right here!
        for component in self.components:
            cls = getattr(component, "class_name", None)
            if cls in theme_dict:
                for property_name, value in theme_dict[cls].items():
                    component.update_style(property_name, value)
        
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
            state._PENDING_JS.append(js_script)

    # =====================================================================
    # LIFECYCLE MANAGEMENT
    # =====================================================================
    def run(self, **kwargs):
        # The base HTML is just an empty canvas with pywebview's API bridge ready
        base_html = settings.BASE_HTML
        
        # Create the JS API bridge so frontend clicks can talk to Python functions
        class JSBridge:
            # def trigger_event(self, event_id, params=None, data={}):
            #     """A universal event handler for every single widget."""
            #     if event_id in state.EVENT_REGISTRY:
            #         cb = state.EVENT_REGISTRY[event_id]['callback']
            #         state.EVENT_REGISTRY[event_id]['data'] = data
            #         # If the widget sent data (like text or a slider value), pass it to Python
            #         if cb:
            #             if params is not None:
            #                 cb(params)
            #             else:
            #                 cb() # Standard click with no data
            def trigger(self, event_id, params=None, data=None):

                # -------------------------
                # 1. FUTURE RESOLVE (async get_info)
                # -------------------------
                if data and "req_id" in data:
                    req_id = data["req_id"]

                    future = state._FUTURES.get(req_id)
                    if future:
                        future["value"] = data
                        future["done"] = True

                # -------------------------
                # 2. DEBOUNCE EVENT (STOP DOUBLE FIRING)
                # -------------------------
                now = time.time()
                last = state._LAST_EVENT_TIME.get(event_id, 0)

                if now - last < 0.05:   # 50ms protection
                    return

                state._LAST_EVENT_TIME[event_id] = now

                # -------------------------
                # 3. RUN CALLBACK
                # -------------------------
                cb = state.EVENT_HANDLERS.get(event_id)

                if cb:
                    try:
                        if params is not None and data is not None:
                            cb(params, data)
                        elif params is not None:
                            cb(params)
                        elif data is not None:
                            cb(data)
                        else:
                            cb()
                    except Exception as e:
                        print("Callback error:", e)

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
        webview.start(self._on_loaded, **kwargs)
    
    def _on_loaded(self):
        self._initial_render()

    def _initial_render(self):
        for comp in self.components:
            comp.app = self  # Ensure cascading reference matching
            comp.render()
        
        # 🔥 execute queued JS
       
        for js in state._PENDING_JS:
            self.window.evaluate_js(js)

        state._PENDING_JS.clear()

         # small delay ensures JS runtime is ready
        self.window.evaluate_js("""
            setTimeout(() => {
                window.pywebviewReady = true;
            }, 50);
        """)

       