from webGui.html.tags import Input

class TextInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'text'
        super().__init__(attrs=attrs, style=style, **kwargs)


class PasswordInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'password'
        super().__init__(attrs=attrs, style=style, **kwargs)


class EmailInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'email'
        super().__init__(attrs=attrs, style=style, **kwargs)


class NumberInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'number'
        super().__init__(attrs=attrs, style=style, **kwargs)


class CheckboxInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'checkbox'
        super().__init__(attrs=attrs, style=style, **kwargs)


class RadioInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'radio'
        super().__init__(attrs=attrs, style=style, **kwargs)


class FileInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'file'
        super().__init__(attrs=attrs, style=style, **kwargs)


class DateInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'date'
        super().__init__(attrs=attrs, style=style, **kwargs)


class ColorInput(Input):
    def __init__(self, attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs['type'] = 'color'
        super().__init__(attrs=attrs, style=style, **kwargs)


class InputField(Input):
    def __init__(self, input_type="text", attrs=None, style=None, **kwargs):
        attrs = attrs or {}
        attrs["type"] = input_type
        super().__init__(attrs=attrs, style=style, **kwargs)


class RangeInput(Input):
    def __init__(self, attrs={}, min=0, max=100, step=1, **kwargs):
       
        attrs["type"] = "range"
        attrs["min"] = str(min)
        attrs["max"] = str(max)
        attrs["step"] = str(step)

        super().__init__(attrs=attrs, **kwargs)