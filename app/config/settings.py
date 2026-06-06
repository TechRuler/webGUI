# settings.py

# Default Window Settings
DEFAULT_TITLE = "My Pure Python App"
DEFAULT_WIDTH = 800
DEFAULT_HEIGHT = 600

# Global UI Theme Configuration
THEME = {
    "background_color": "#f5f6fa",
    "font_family": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    "primary_button_color": "#3498db",
    "text_color": "#333333"
}

# The single Base HTML Canvas template used across the framework
BASE_HTML = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body, html {{
            margin: 0; 
            padding: 0; 
            width: 100%; 
            height: 100%;
            font-family: {THEME['font_family']};
            background-color: {THEME['background_color']};
            color: {THEME['text_color']};
            overflow-x: hidden; /* Prevents ugly horizontal scrollbars */
        }}
        
        /* #root is now a pure, invisible, full-bleed window container */
        #root {{
            display: flex; 
            flex-direction: column; 
            width: 100%; 
            height: 100%;
            margin: 0;
            padding: 0; /* 👈 Removed 20px padding to fix edge margins! */
            box-sizing: border-box;
            align-items: stretch; /* 👈 Changed from flex-start so child layouts fill width */
            justify-content: flex-start;
        }}
    </style>
</head>
<body>
    <div id="root"></div>
</body>
</html>
"""