import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from webGui.main import App
# from webGui.widgets import Button
# from webGui.widgets.label import Label
# from webGui.widgets import HorizontalFrame, VerticalFrame, Grid

# # 1. Initialize our main worackgroundColorcanvas
# app = App(title="Layout Engine: Axis Comparisons", width=950, height=650)

# # 2. The Master Stacker (Vertical)
# # This forces the top bar section to sit strictly above our grid section.
# master_stack = VerticalFrame(alignment="stretch", gap="35px")


# # =====================================================================
# # SCENE 1: THE HORIZONTAL AXIS (One-Dimensional Flow)
# # =====================================================================
# # Notice how the buttons adapt strictly to their contents. They don't 
# # care about matching sizes; they just line up neatly left-to-right.
# top_navbar = HorizontalFrame(alignment="space-between", style={"background": "#2c3e50", "padding": "15px"})

# logo = Label("📊 System Matrix", style={"fontSize": "20px", "fontWeight": "bold", "color": "#ffffff"})
# nav_actions = HorizontalFrame(gap="12px")

# btn_refresh = Button("Refresh Core", backgroundColor="#2980b9", border="none", borderRadius="6px", padding="6px")
# btn_logs = Button("View Historical Error Logs Database", backgroundColor="#34495e", border="none", borderRadius="6px", padding="6px") # Long text expands naturally

# nav_actions.add(btn_refresh)
# nav_actions.add(btn_logs)
# top_navbar.add(logo)
# top_navbar.add(nav_actions)


# # =====================================================================
# # SCENE 2: THE GRID AXIS (Two-Dimbensional Matrix)
# # =====================================================================
# # No matter how long or short the button texts are, this layout forcing 
# # mechanism locks them into 3 perfectly matching geometric columns.
# dashboard_grid = Grid(columns="repeat(3, 1fr)", style={"padding": "0 20px","gap":"20px"})

# # Row 1 of Grid
# card_a = Button("CPU Load: 42%", backgroundColor="#2ecc71", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_b = Button("RAM Usage: 8GB / 16GB", backgroundColor="#3498db", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_c = Button("Disk I/O: Steady", backgroundColor="#9b59b6", style={"height": "140px", "width": "100%", "fontSize": "18px"})

# # Row 2 of Grid (Will automatically break downward and realign perfectly under Row 1)
# card_d = Button("Active Threads", backgroundColor="#1abc9c", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_e = Button("SQL Queries Pool", backgroundColor="#e67e22", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_f = Button("Network Latency", backgroundColor="#e74c3c", style={"height": "140px", "width": "100%", "fontSize": "18px"})

# dashboard_grid.add(card_a)
# dashboard_grid.add(card_b)
# dashboard_grid.add(card_c)
# dashboard_grid.add(card_d)
# dashboard_grid.add(card_e)
# dashboard_grid.add(card_f)


# # =====================================================================
# # ASSEMBLY AND RUNTIME
# # =====================================================================
# # Stack the top section and grid section inside our master vertical scope
# master_stack.add(top_navbar)
# master_stack.add(dashboard_grid)

# # Send it to the engine frame!
# app.add(master_stack)
# app.run()

from webGui import App
from webGui.widgets.button import Button
from webGui.widgets.label import Label
# from webGui.widgets.layout import Horizontal, Vertical
from webGui.widgets import HorizontalFrame, VerticalFrame

# 1. Initialize our main app canvas framework
app = App(title="Dynamic Theme Switcher", width=600, height=300)

# =====================================================================
# CALLBACK LOGIC (Interacts directly with app attributes)
# =====================================================================
def apply_dark_mode():
    app.set_title("Core Dashboard (Dark Mode)")
    app.set_background("#1e272e") # Dark slate slate blue
    title_text.innerText("Dark Mode Theme Active")

def apply_light_mode():
    app.set_title("Core Dashboard (Light Mode)")
    app.set_background("#f5f6fa") # Default soft framework white
    title_text.innerText("Light Mode Theme Active")

def apply_matrix_mode():
    app.set_title("⚡ ENCRYPTED CONSOLE ⚡")
    app.set_background("#000000") # Pure pitch black
    title_text.innerText("Matrix Overhaul Implemented")

# =====================================================================
# LAYOUT STRUCTURAL ASSEMBLY
# =====================================================================
master_stack = VerticalFrame(alignment="center", gap="25px", padding="30px")

title_text = Label("Select an Application Theme Profile Below", style={"fontSize": "20px", "fontWeight": "bold"})
theme_bar = HorizontalFrame(gap="15px", backgroundColor="#dcdde1", padding="20px", borderRadius="8px")

# Instantiate control buttons
btn_dark = Button("Go Dark", backgroundColor="#2c3e50",color="white",padding="10px 20px",border="none",borderRadius="6px",cursor="pointer",width="max-content",fontSize="16px",trainsition="filter 0.2s", on_click=apply_dark_mode)
btn_light = Button("Go Light", backgroundColor="#dcdde1",color="white",padding="10px 20px",border="none",borderRadius="6px",cursor="pointer",width="max-content",fontSize="16px",trainsition="filter 0.2s", on_click=apply_light_mode)
btn_matrix = Button("Go Matrix", backgroundColor="#4cd137",color="white",padding="10px 20px",border="none",borderRadius="6px",cursor="pointer",width="max-content",fontSize="16px",trainsition="filter 0.2s", on_click=apply_matrix_mode)

# Add elements manually to build the node tree hierarchy
theme_bar.add(btn_dark)
theme_bar.add(btn_light)
theme_bar.add(btn_matrix)

master_stack.add(title_text)
master_stack.add(theme_bar)
btn = Button(text='get')
def func():
    print(btn_dark.dom.innerText())
    
btn.on('click',func)


# Boot up the window application pipeline
app.add(master_stack)

app.add(btn)
app.run()
