import webview

window = webview.create_window("My App", "https://google.com")

menu = [
    webview.menu.Menu(
        'File',
        [
            webview.menu.MenuAction('Open', lambda: print('Open')),
            webview.menu.MenuAction('Exit', webview.windows[0].destroy)
        ]
    )
]

webview.start(menu=menu)