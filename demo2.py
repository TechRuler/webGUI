from app.main import App
from app.widgets.animation import Animation
from app.widgets import Button
root = App(title="App", width=800, height=600)

fade = Animation(
    app=root,
    name="pulse",
    keyframes="""
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    """,
    duration="1s",
    timing="ease-in-out",
    iteration="infinite"
)

fade.register()

# root.set_background("linear-gradient(to right, #ff512f, #dd2476)")

button = Button(text="yes", bg_color="red", style={"margin":"20px"})

fade.apply(button.id)

root.add(button)

root.run()