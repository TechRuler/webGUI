import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from webGui import App
from webGui.widgets import Frame
from webGui.core import Animation

# 1. Canvas Frame Initialization
root = App(title="3D Rotating Cube Matrix", width=800, height=600)
root.set_background("#111116") # Deep dark tech space background

# 2. Define the 360-degree Continuous 3D Rotation Animation Loop
rotate_3d = Animation(
    app=root,
    name="spin3D",
    keyframes="""
        0% { transform: rotateX(0deg) rotateY(0deg) rotateZ(0deg); }
        100% { transform: rotateX(360deg) rotateY(360deg) rotateZ(360deg); }
    """,
    duration="6s",
    timing="linear",
    iteration="infinite"
)
rotate_3d.register()

# 3. Perspective Stage Container Block (This makes the 3D depth work!)
stage = Frame(style={
    "position": "absolute",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)",
    "perspective": "800px",  # Gives depth perspective to the scene
    "width": "300px",
    "height": "300px",
    "display": "flex",
    "alignItems": "center",
    "justifyContent": "center"
})
root.add(stage)

# 4. The Main Cube Core Node
with stage:
    cube = Frame(style={
        "position": "relative",
        "width": "200px",
        "height": "200px",
        "transformStyle": "preserve-3d", # CRITICAL: Keeps child faces inside 3D environment space
    })

# 5. Define the inFrameidual transforms and colors for the 6 faces
# Every face shifts out by exactly half the cube's width (100px) from the center origin
face_configs = [
    {"transform": "rotateY(0deg) translateZ(100px)",   "bg": "rgba(231, 76, 60, 0.7)",  "border": "#e74c3c"},  # Front
    {"transform": "rotateY(180deg) translateZ(100px)", "bg": "rgba(52, 152, 219, 0.7)", "border": "#3498db"}, # Back
    {"transform": "rotateY(90deg) translateZ(100px)",  "bg": "rgba(46, 204, 113, 0.7)", "border": "#2ecc71"},  # Right
    {"transform": "rotateY(-90deg) translateZ(100px)", "bg": "rgba(241, 196, 15, 0.7)", "border": "#f1c40f"},  # Left
    {"transform": "rotateX(90deg) translateZ(100px)",  "bg": "rgba(155, 89, 182, 0.7)", "border": "#9b59b6"},  # Top
    {"transform": "rotateX(-90deg) translateZ(100px)", "bg": "rgba(26, 188, 156, 0.7)", "border": "#1abc9c"}   # Bottom
]

# 6. Build the Faces Inside the Cube Block Architecture context
with cube:
    for config in face_configs:
        Frame(style={
            "position": "absolute",
            "width": "200px",
            "height": "200px",
            "backgroundColor": config["bg"],
            "border": f"2px solid {config['border']}",
            "transform": config["transform"], # Injects direct matrix translations 
            "boxShadow": f"0 0 20px {config['border']}33",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center",
            "color": "white",
            "fontSize": "20px",
            "fontFamily": "sans-serif",
            "userSelect": "none"
        })

# 7. Apply the global 3D infinite rotation setup to the parent cube node wrapper
rotate_3d.apply(cube.id)

# Launch native canvas layout frames
root.run()