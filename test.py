from webGui.widgets.button import Button
from webGui.widgets.label import Label
from webGui.layout import HorizontalDiv

# 1. Create a button with specific configurations and layout rules
button = Button(
    text="Launch Matrix", 
    class_name="btn-primary", 
    backgroundColor="#e74c3c", 
    borderRadius="12px"
)

# 2. Read direct Python properties
print(button.get_config("text"))         # Output: Launch Matrix
print(button.get_config("class_name"))    # Output: btn-primary

# 3. Read nested CSS kwargs properties
print(button.get_config("backgroundColor")) # Output: #e74c3c
print(button.get_config("borderRadius"))    # Output: 12px

# 4. Read an unknown value safely without crashing
button.update_style("padding", "100px 100px") # Dynamically add a new style property
print(button.get_config("padding"))      # Output: None (or default value if set)