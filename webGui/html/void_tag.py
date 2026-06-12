import json
from webGui.core.base import BaseWidget


class VoidTag(BaseWidget):
    def __init__(
        self,
        tag="",
        attrs=None,
        class_name="",
        style=None,
        **kwargs
    ):
        super().__init__(
            prefix=tag,
            style=style,
            class_name=class_name,
            **kwargs
        )

        self.tag = tag
        self.attrs = attrs or {}

    def render(self):
        window = self.get_window()
        if not window:
            return

        parent_target = getattr(self, "_target_parent_id", "root")

        js = f"""
        (function(){{
            let element = document.createElement('{self.tag}');
            element.id = '{self.id}';

            const cls = {json.dumps(self.class_name)};
            if (cls && cls.trim()) {{
                element.classList.add(...cls.trim().split(/\\s+/));
            }}

            Object.assign(element.style, {json.dumps(self.style)});

            const attrs = {json.dumps(self.attrs)};
            for (const [key, value] of Object.entries(attrs)) {{
                if (value !== null && value !== undefined) {{
                    element.setAttribute(key, value);
                }}
            }}

            document.getElementById('{parent_target}')
                .appendChild(element);
        }})();
        """

        window.evaluate_js(js)

        self._mark_rendered()