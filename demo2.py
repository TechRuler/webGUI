from webGui import App 

from webGui.html import Button

root = App(title="App", width=800, height=600)


btn = Button(padding="20px", backgroundColor="red", fontSize="20px", width='max-content')
btn.textContent(text="he")


root.add(btn)


root.run()