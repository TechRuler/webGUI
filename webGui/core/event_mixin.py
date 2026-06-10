import json
from webGui.config import state
class EventMixin:

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