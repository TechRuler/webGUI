from webGui import App
from webGui.core import Animation
from webGui.widgets import Button
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

button = Button(text="yes", bg_color="red", font_size="24px", padding="15px 30px", on_click=lambda: root.set_background("linear-gradient(to right, #ff512f, #dd2476)")  , border_radius="12px", border="2px solid black")

# fade.apply(button.id)

button.on("click", lambda: button.update_style("backgroundColor", "green"))


root.add(button)



root.run()