import json

class DOMMixin:

    

    def innerText(self, text: str):
        self._execute_js(f"document.getElementById('{self.id}').innerText = {json.dumps(text)};")
        return self
    
    def innerHTML(self, html: str):
        self._execute_js(
            f"document.getElementById('{self.id}').innerHTML = {json.dumps(html)};"
        )
        return self
    def textContent(self, text: str):
        self._execute_js(
            f"document.getElementById('{self.id}').textContent = {json.dumps(text)};"
        )
        return self
    
    def add_class(self, class_name: str):
        self._execute_js(
            f"document.getElementById('{self.id}').classList.add({json.dumps(class_name)});"
        )
        return self
    
    def remove_class(self, class_name: str):
        self._execute_js(
            f"document.getElementById('{self.id}').classList.remove({json.dumps(class_name)});"
        )
        return self
    def toggle_class(self, class_name: str):
        self._execute_js(
            f"document.getElementById('{self.id}').classList.toggle({json.dumps(class_name)});"
        )
        return self
    def set_style(self, key: str, value):
        self._execute_js(
            f"document.getElementById('{self.id}').style[{json.dumps(key)}] = {json.dumps(value)};"
        )
        return self
    def set_attribute(self, name: str, value):
        self._execute_js(
            f"document.getElementById('{self.id}').setAttribute({json.dumps(name)}, {json.dumps(value)});"
        )
        return self
    def remove_attribute(self, name: str):
        self._execute_js(
            f"document.getElementById('{self.id}').removeAttribute({json.dumps(name)});"
        )
        return self