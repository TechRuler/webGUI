# from app.main import App
# from app.widgets.button import Button
# from app.widgets.label import Label
# from app.layout import Horizontal, Vertical, Grid

# # 1. Initialize our main workspace canvas
# app = App(title="Layout Engine: Axis Comparisons", width=950, height=650)

# # 2. The Master Stacker (Vertical)
# # This forces the top bar section to sit strictly above our grid section.
# master_stack = Vertical(alignment="stretch", gap="35px")


# # =====================================================================
# # SCENE 1: THE HORIZONTAL AXIS (One-Dimensional Flow)
# # =====================================================================
# # Notice how the buttons adapt strictly to their contents. They don't 
# # care about matching sizes; they just line up neatly left-to-right.
# top_navbar = Horizontal(alignment="space-between", style={"background": "#2c3e50", "padding": "15px"})

# logo = Label("📊 System Matrix", style={"fontSize": "20px", "fontWeight": "bold", "color": "#ffffff"})
# nav_actions = Horizontal(gap="12px")

# btn_refresh = Button("Refresh Core", bg_color="#2980b9")
# btn_logs = Button("View Historical Error Logs Database", bg_color="#34495e") # Long text expands naturally

# nav_actions.add(btn_refresh)
# nav_actions.add(btn_logs)
# top_navbar.add(logo)
# top_navbar.add(nav_actions)


# # =====================================================================
# # SCENE 2: THE GRID AXIS (Two-Dimensional Matrix)
# # =====================================================================
# # No matter how long or short the button texts are, this layout forcing 
# # mechanism locks them into 3 perfectly matching geometric columns.
# dashboard_grid = Grid(columns="repeat(3, 1fr)", gap="20px", style={"padding": "0 20px"})

# # Row 1 of Grid
# card_a = Button("CPU Load: 42%", bg_color="#2ecc71", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_b = Button("RAM Usage: 8GB / 16GB", bg_color="#3498db", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_c = Button("Disk I/O: Steady", bg_color="#9b59b6", style={"height": "140px", "width": "100%", "fontSize": "18px"})

# # Row 2 of Grid (Will automatically break downward and realign perfectly under Row 1)
# card_d = Button("Active Threads", bg_color="#1abc9c", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_e = Button("SQL Queries Pool", bg_color="#e67e22", style={"height": "140px", "width": "100%", "fontSize": "18px"})
# card_f = Button("Network Latency", bg_color="#e74c3c", style={"height": "140px", "width": "100%", "fontSize": "18px"})

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
from webGui.layout import Horizontal, Vertical

# 1. Initialize our main app canvas framework
app = App(title="Dynamic Theme Switcher", width=600, height=300)

# =====================================================================
# CALLBACK LOGIC (Interacts directly with app attributes)
# =====================================================================
def apply_dark_mode():
    app.set_title("Core Dashboard (Dark Mode)")
    app.set_background("#1e272e") # Dark slate slate blue
    title_text.update_text("Dark Mode Theme Active")

def apply_light_mode():
    app.set_title("Core Dashboard (Light Mode)")
    app.set_background("#f5f6fa") # Default soft framework white
    title_text.update_text("Light Mode Theme Active")

def apply_matrix_mode():
    app.set_title("⚡ ENCRYPTED CONSOLE ⚡")
    app.set_background("#000000") # Pure pitch black
    title_text.update_text("Matrix Overhaul Implemented")

# =====================================================================
# LAYOUT STRUCTURAL ASSEMBLY
# =====================================================================
master_stack = Vertical(alignment="center", gap="25px", style={"padding": "30px"})

title_text = Label("Select an Application Theme Profile Below", style={"fontSize": "20px", "fontWeight": "bold"})
theme_bar = Horizontal(gap="15px")

# Instantiate control buttons
btn_dark = Button("Go Dark", bg_color="#2c3e50", on_click=apply_dark_mode)
btn_light = Button("Go Light", bg_color="#dcdde1", on_click=apply_light_mode)
btn_matrix = Button("Go Matrix", bg_color="#4cd137", on_click=apply_matrix_mode)

# Add elements manually to build the node tree hierarchy
theme_bar.add(btn_dark)
theme_bar.add(btn_light)
theme_bar.add(btn_matrix)

master_stack.add(title_text)
master_stack.add(theme_bar)

# Boot up the window application pipeline
app.add(master_stack)
app.run()