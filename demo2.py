from webGui import App
from webGui.core import Animation
from webGui.widgets import Button, InputField, Label
root = App(title="App", width=800, height=600)

# fade = Animation(
#     app=root,
#     name="pulse",
#     keyframes="""
#         0% { transform: scale(1); }
#         50% { transform: scale(1.1); }
#         100% { transform: scale(1); }
#     """,
#     duration="1s",
#     timing="ease-in-out",
#     iteration="infinite"
# )

# fade.register()

# root.set_background("linear-gradient(to right, #ff512f, #dd2476)")

# button = Button(text="yes",)

# # fade.apply(button.id)

# # button.on("click", lambda: button.update_style("backgroundColor", "green"))


# root.add(button)
label = Label(text='Input', class_name="name")
entry = InputField(placeholder='text', class_name="entry", backgroundColor="red", color="white", borderColor="green", borderRadius = "6px" , margin="40px", fontSize="26px", fontFamily="Fira Code")
print(label.get_info('text'))
entry.on('input', lambda: label.update_text(entry.get_info('value')))
# print(entry.get_info('tag'))
button = Button(text='yess')
button.on('click', lambda: print(label.get_info('class')))
# word = None
root.add(label)
root.add(entry)
root.add(button)



root.run()