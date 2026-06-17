from webGui.html.tags import Select, Option

class ComboBox(Select):
    def __init__(self, options=None, class_name=None, style=None, **kwargs):
        super().__init__(class_name=class_name, style=style, **kwargs)

        self.options = []

        self.add_item('Select Language')
        self.add_items(options or [])
    
    def add_items(self, options=None):
        for option in options or []:
            self.add_item(option)
    
    def add_item(self, option):
        op = Option()

        if isinstance(option, str):
            op.innerText(option)
            op.value(option)

        elif isinstance(option, dict):
            op.innerText(option.get("text", ""))
            op.value(option.get("value", option.get("text", "")))
        else:
            print(f"{type(option)} is not allowed")

        self.add(op)
        self.options.append(op)
        
    def clear_items(self):
        self.clear()
        self.options.clear()
        return self
    
    def get_option(self, index):
        return self.options[index]
    
    def get_options(self):
        return self.options
    
    def count(self):
        return len(self.options)