class StyleMixin:

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

    def update_style(self, property_name, value):
        """A universal method allowing users to change ANY CSS property on the fly!"""
        self.style[property_name] = value
        window = self.get_window()
        if window:
            js_update = f"document.getElementById('{self.id}').style.{property_name} = '{value}';"
            window.evaluate_js(js_update)