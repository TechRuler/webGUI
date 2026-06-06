class Animation:
    def __init__(self, app, name, keyframes, duration="1s", timing="ease", iteration="1"):
        self.app = app
        self.name = name
        self.keyframes = keyframes
        self.duration = duration
        self.timing = timing
        self.iteration = iteration

    # -----------------------------
    # Inject keyframes globally
    # -----------------------------
    def register(self):
        js = f"""
        (function() {{
            let style = document.createElement('style');
            style.innerHTML = `
            @keyframes {self.name} {{
                {self.keyframes}
            }}
            `;
            document.head.appendChild(style);
        }})();
        """

        if self.app.window:
            self.app.window.evaluate_js(js)
        else:
            self.app._pending_js.append(js)

    # -----------------------------
    # Apply animation to widget
    # -----------------------------
    def apply(self, widget_id):
        js = f"""
        (function() {{
            let el = document.getElementById("{widget_id}");
            if (!el) return;

            el.style.animation = "{self.name} {self.duration} {self.timing} {self.iteration}";
        }})();
        """

        if self.app.window:
            self.app.window.evaluate_js(js)
        else:
            self.app._pending_js.append(js)