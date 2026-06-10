import webview

def hello():
    print("Hello clicked!")

def about():
    print("About clicked!")

menu = [
    {
        'label': 'File',
        'submenu': [
            {'label': 'Hello', 'action': hello},
            {'label': 'Exit', 'action': lambda: webview.destroy_window()}
        ]
    },
    {
        'label': 'Help',
        'submenu': [
            {'label': 'About', 'action': about}
        ]
    }
]

webview.create_window(
    title="My App",
    html="<body style='background:black;color:white;'>Hello</body>",
    width=800,
    height=600,
    menu=menu
)

# 👇 FORCE backend
webview.start(gui='edgechromium')   # Windows best option