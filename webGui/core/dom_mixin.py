import json
_SENTINEL = object()
class DOMMixin:

    _css_rules = {}

    def _el(self):
        return f"document.getElementById('{self.id}')"
    
    def _property(self, name, value=_SENTINEL):
        if value is not _SENTINEL:
            self._run_dom_js(
                f"{self._el()}.{name} = {json.dumps(value)};"
            )
            return self
        
        return self._run_dom_js(
            f"{self._el()}.{name};"
        )
    
    def add_css_rule(self, selector, styles):
        self._css_rules[selector] = styles

        css = []

        for selector, styles in self._css_rules.items():
            css.append(f"{selector} {{")

            for key, value in styles.items():
                if key == "content":
                    value = f'"{value}"'

                css.append(f"    {key}: {value};")

            css.append("}")

        css_text = "\n".join(css)

        self._run_dom_js(f"""
        (() => {{
            let style = document.getElementById("dommixin-styles");

            if (!style) {{
                style = document.createElement("style");
                style.id = "dommixin-styles";
                document.head.appendChild(style);
            }}

            style.textContent = {json.dumps(css_text)};
        }})();
        """)

        return self

    def pseudo(self, selector, css):
        self.add_css_rule(f"#{self.id}{selector}", css)
        return self

    def innerText(self, text=_SENTINEL):
        return self._property("innerText", text)

    def innerHTML(self, html=_SENTINEL):
        return self._property("innerHTML", html)

    def textContent(self, text=_SENTINEL):
        return self._property("textContent", text)
    
    def value(self, value=_SENTINEL):
        return self._property("value", value)

    def checked(self, checked=_SENTINEL):
        return self._property("checked", checked)

    def disabled(self, disabled=_SENTINEL):
        return self._property("disabled", disabled)

    def placeholder(self, placeholder=_SENTINEL):
        return self._property("placeholder", placeholder)

    def src(self, src=_SENTINEL):
        return self._property("src", src)

    def href(self, href=_SENTINEL):
        return self._property("href", href)

    def title(self, title=_SENTINEL):
        return self._property("title", title)
    
    def set_id(self, value):
        old_id = self.id

        self._run_dom_js(
            f"document.getElementById('{old_id}').id = {json.dumps(value)};"
        )
        self.id = value
        return self

    def className(self, value=_SENTINEL):
        return self._property("className", value)

    def readOnly(self, value=_SENTINEL):
        return self._property("readOnly", value)

    def selected(self, value=_SENTINEL):
        return self._property("selected", value)

    def tabIndex(self, value=_SENTINEL):
        return self._property("tabIndex", value)
    
    def store_data(self, name:str, value=_SENTINEL):
        if value is not _SENTINEL:
            self._run_dom_js(
                f"{self._el()}.dataset[{json.dumps(name)}] = {json.dumps(value)};"
            )
            return self

        return self._run_dom_js(
            f"{self._el()}.dataset[{json.dumps(name)}];"
        )
    def remove(self):
        self._run_dom_js(
            f"{self._el()}.remove();"
        )
        return self
    def focus(self):
        self._run_dom_js(
            f"{self._el()}.focus();"
        )
        return self
    def blur(self):
        self._run_dom_js(
            f"{self._el()}.blur();"
        )
        return self
    def show(self):
        self._run_dom_js(
            f"{self._el()}.style.display = '';"
        )
        return self

    def hide(self):
        self._run_dom_js(
            f"{self._el()}.style.display = 'none';"
        )
        return self
    def click(self):
        self._run_dom_js(
            f"{self._el()}.click();"
        )
        return self
    def append_html(self, html: str):
        self._run_dom_js(
            f"{self._el()}.insertAdjacentHTML('beforeend', {json.dumps(html)});"
        )
        return self
    def clear(self):
        self._run_dom_js(
            f"{self._el()}.innerHTML = '';"
        )
        return self
    def scroll_into_view(self):
        self._run_dom_js(
            f"{self._el()}.scrollIntoView();"
        )
        return self
    def exists(self):
        return self._run_dom_js(
            f"document.getElementById('{self.id}') !== null;"
        )
    def parent_element(self):
        return self._run_dom_js(
            f"{self._el()}.parentElement?.id;"
        )
    def children_count(self):
        return self._run_dom_js(
            f"{self._el()}.children.length;"
        )
    def filter(self, value: str):
        self.set_style("filter", value)
        return self

    def add_class(self, class_name: str):
        self._run_dom_js(
            f"{self._el()}.classList.add({json.dumps(class_name)});"
        )
        return self
    def get_class(self):
        return self._run_dom_js(
            f"Array.from({self._el()}.classList);"
        )
    def remove_class(self, class_name: str):
        self._run_dom_js(
            f"{self._el()}.classList.remove({json.dumps(class_name)});"
        )
        return self
    def toggle_class(self, class_name: str):
        self._run_dom_js(
            f"{self._el()}.classList.toggle({json.dumps(class_name)});"
        )
        return self
    
    def set_style(self, key: str, value):
        self._run_dom_js(
            f"""
            (() => {{
                const el = {self._el()};
                if (el) {{
                    el.style[{json.dumps(key)}] = {json.dumps(value)};
                }}
            }})();
            """
        )
        return self
    def set_styles(self, css):
        js = []

        for k, v in css.items():
            js.append(
                f"el.style[{json.dumps(k)}] = {json.dumps(v)};"
            )

        self._run_dom_js(f"""
        (() => {{
            const el = {self._el()};
            if (el) {{
                {" ".join(js)}
            }}
        }})();
        """)

        return self
    def get_style(self, key: str):
        return self._run_dom_js(
            f"getComputedStyle({self._el()})[{json.dumps(key)}];"
        )
    
    def set_attribute(self, name: str, value):
        self._run_dom_js(
            f"{self._el()}.setAttribute({json.dumps(name)}, {json.dumps(value)});"
        )
        return self
    def has_attribute(self, name: str):
        return self._run_dom_js(
            f"{self._el()}.hasAttribute({json.dumps(name)});"
        )
    def get_attribute(self, name: str):
        return self._run_dom_js(
            f"{self._el()}.getAttribute({json.dumps(name)});"
        )
    def remove_attribute(self, name: str):
        self._run_dom_js(
            f"{self._el()}.removeAttribute({json.dumps(name)});"
        )
        return self
    
    def before(self, css):
        return self.pseudo("::before", css)

    def after(self, css):
        return self.pseudo("::after", css)

    def focus_css(self, css):
        return self.pseudo(":focus", css)

    def hover_css(self, css):
        return self.pseudo(":hover", css)

    def active_css(self, css):
        return self.pseudo(":active", css)