from webGui import App
from webGui.layout import Div
from webGui.core import Animation

# 1. Canvas Frame Initialization
root = App(title="Cosmic Solar System Engine", width=900, height=700)
root.set_background("#0b0b12") # Outer space deep black/purple tint

# =====================================================================
# 2. REGISTER ORBIT ROTATION SYSTEM TRACKS
# =====================================================================
# We define distinct speeds for each planet orbit loop
orbit_speeds = {"mercury": "1.5s", "venus": "3s", "earth": "5s", "mars": "7s"}
orbit_animations = {}

for planet, speed in orbit_speeds.items():
    anim = Animation(
        app=root,
        name=f"orbit_{planet}",
        keyframes="""
            0% { transform: translate(-50%, -50%) rotate(0deg); }
            100% { transform: translate(-50%, -50%) rotate(360deg); }
        """,
        duration=speed,
        timing="linear",
        iteration="infinite"
    )
    anim.register()
    orbit_animations[planet] = anim

# =====================================================================
# 3. BUILD THE STRUCTURE LAYOUT
# =====================================================================
# Main Space Canvas Centering Frame Anchor
space_canvas = Div(style={
    "position": "absolute",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)",
    "width": "600px",
    "height": "600px"
})
root.add(space_canvas)

with space_canvas:
    # 🌟 THE CENTRAL SUN
    # It sits perfectly centered using transform positions
    sun = Div(style={
        "position": "absolute",
        "top": "50%",
        "left": "50%",
        "transform": "translate(-50%, -50%)",
        "width": "60px",
        "height": "60px",
        "backgroundColor": "#f1c40f",
        "borderRadius": "50%",
        "boxShadow": "0 0 40px #f39c12, 0 0 10px #f1c40f",
        "zIndex": "10"
    })

    # 🪐 PLANET SPECIFICATIONS PROFILE CONFIG MATRIX
    # radius: the size of the planetary orbit ring circle boundary
    # size: the width/height diameter of the planet body node
    # color: the hex graphic shader profile matching the planet archetype
    planet_matrix = [
        {"name": "mercury", "radius": 130, "size": 12, "color": "#95a5a6"},
        {"name": "venus",   "radius": 200, "size": 18, "color": "#e67e22"},
        {"name": "earth",   "radius": 280, "size": 22, "color": "#3498db"},
        {"name": "mars",    "radius": 370, "size": 16, "color": "#e74c3c"}
    ]

    # Dynamically inject the planet nodes inside the space canvas container context
    for p in planet_matrix:
        # Create the rotating orbit wrapper boundary ring line
        orbit_ring = Div(style={
            "position": "absolute",
            "top": "50%",
            "left": "50%",
            "transform": "translate(-50%, -50%)",
            "width": f"{p['radius']}px",
            "height": f"{p['radius']}px",
            "border": "1px dashed rgba(255, 255, 255, 0.12)",
            "borderRadius": "50%",
            "pointerEvents": "none" # Clicks pass right through the invisible ring lines
        })
        
        # Place the physical planet body right onto its parent orbit container edge
        with orbit_ring:
            Div(style={
                "position": "absolute",
                "top": "50%",
                "left": "100%", # Pulls it straight out to the far right perimeter boundary edge
                "transform": "translate(-50%, -50%)",
                "width": f"{p['size']}px",
                "height": f"{p['size']}px",
                "backgroundColor": p["color"],
                "borderRadius": "50%",
                "boxShadow": f"0 0 10px {p['color']}88"
            })
            
        # Apply the matching infinite circular keyframe animation straight to the container ring node
        orbit_animations[p["name"]].apply(orbit_ring.id)

# Spin up your native framework window
root.run()