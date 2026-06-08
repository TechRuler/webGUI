from webGui import App
from webGui.layout import Div
from webGui.core import Animation

# 1. Canvas and Background setup
root = App(title="Quantum 3D Atom Core", width=800, height=600)
root.set_background("#09090e") # Deep subatomic void space

# =====================================================================
# 2. SUBATOMIC ROTATION TRACKS
# =====================================================================
# Orbit spin animation: Forces a continuous 360-degree rotation loop
electron_spin = Animation(
    app=root,
    name="electronSpin",
    keyframes="""
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    """,
    duration="2s",
    timing="linear",
    iteration="infinite"
)
electron_spin.register()

# Nucleus shimmer animation: Makes the core energy particles breathe/pulse
nucleus_pulse = Animation(
    app=root,
    name="nucleusPulse",
    keyframes="""
        0% { transform: translate(-50%, -50%) scale(1); filter: brightness(1); }
        50% { transform: translate(-50%, -50%) scale(1.08); filter: brightness(1.3); }
        100% { transform: translate(-50%, -50%) scale(1); filter: brightness(1); }
    """,
    duration="1.5s",
    timing="ease-in-out",
    iteration="infinite"
)
nucleus_pulse.register()

# =====================================================================
# 3. CONSTRUCT THE ATOMIC TREE
# =====================================================================
# Main 3D Container Stage
atom_stage = Div(style={
    "position": "absolute",
    "top": "50%",
    "left": "50%",
    "transform": "translate(-50%, -50%)",
    "width": "500px",
    "height": "500px",
    "perspective": "1000px" # Gives depth to the tilted orbit tracks
})
root.add(atom_stage)

with atom_stage:
    # ⚛️ THE NUCLEUS (Central Energy Core)
    nucleus = Div(style={
        "position": "absolute",
        "top": "50%",
        "left": "50%",
        "transform": "translate(-50%, -50%)",
        "width": "45px",
        "height": "45px",
        "backgroundColor": "#ff007f",
        "borderRadius": "50%",
        "boxShadow": "0 0 35px #ff007f, 0 0 15px #ff007f, inset 0 0 10px #ffffff",
        "zIndex": "10"
    })
    nucleus_pulse.apply(nucleus.id)

    # 💫 ELECTRON ORBIT SPECIFICATIONS MATRIX
    # We tilt each orbit ring differently along the 3D planes (X and Y axis)
    orbit_planes = [
        {"name": "orbit_alpha", "tilt": "rotateX(70deg) rotateY(15deg)"},
        {"name": "orbit_beta",  "tilt": "rotateX(70deg) rotateY(-45deg)"},
        {"name": "orbit_gamma", "tilt": "rotateX(30deg) rotateY(65deg)"}
    ]

    for orbit in orbit_planes:
        # Create a tilted 3D container for the orbit
        orbit_container = Div(style={
            "position": "absolute",
            "top": "0",
            "left": "0",
            "width": "100%",
            "height": "100%",
            "transformStyle": "preserve-3d",
            "transform": orbit["tilt"], # Lock the orientation in 3D space
            "pointerEvents": "none"
        })
        
        with orbit_container:
            # The physical visual ring track that will spin
            ring_track = Div(style={
                "position": "absolute",
                "top": "10%",
                "left": "10%",
                "width": "80%",
                "height": "80%",
                "border": "2px solid rgba(0, 242, 254, 0.25)",
                "borderRadius": "50%",
                "transformStyle": "preserve-3d"
            })
            
            with ring_track:
                # Place the glowing electron particle onto the perimeter of the track
                Div(style={
                    "position": "absolute",
                    "top": "50%",
                    "left": "100%", # Positioned precisely on the far outer border edge
                    "transform": "translate(-50%, -50%)",
                    "width": "14px",
                    "height": "14px",
                    "backgroundColor": "#00f2fe",
                    "borderRadius": "50%",
                    "boxShadow": "0 0 20px #00f2fe, 0 0 5px #ffffff"
                })
                
        # Spin the ring track! Because the track spins inside the tilted container, 
        # the electron sweeps through a beautiful 3D path.
        electron_spin.apply(ring_track.id)

# Execute the application engine framework window
root.run()