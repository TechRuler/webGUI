from webGui import App 
from webGui.widgets import Button, CheckBox
from webGui.layout import Div

root = App(title="App", width=800, height=600)

chbox = CheckBox(text='option 1', display="flex", alignItem="center",gap='6px', width='max-content', margin="20px", padding='20px')
chbox.label_style(color='cyan', backgroundColor="red", fontFamily="Fira Code", padding='5px')
root.add(chbox)
button = Button(text='get value', on_click=lambda:chbox.update_style_label("backgroundColor","blue"), width='max-content')
root.add(button)
root.run()