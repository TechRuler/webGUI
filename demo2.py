from webGui import App 

from webGui.widgets import Text, Button, RadioButton, ToggleSwitch

root = App(title="App", width=800, height=600)

def hover_in(btn):
    btn.filter("brightness(90%)")
def hover_out(btn):
    btn.filter("brightness(100%)")


btn = Button(text='he',padding="20px", backgroundColor="red", fontSize="20px", width='max-content')
# btn.textContent(text="he")
btn_ = Button(text='he',on_click=lambda:btn.set_style("backgroundColor","blue"),padding="20px", backgroundColor="red", fontSize="20px", width='max-content')
# btn_.textContent(text="he")

radio1 = RadioButton(text="Male", group='gender')
radio2 = RadioButton(text="Female", group='gender')
radio3 = RadioButton(text="Other", group='gender')

btn.on('mouseover', lambda:hover_in(btn))
btn.on('mouseout', lambda:hover_out(btn))
btn_.on('mouseover', lambda:hover_in(btn_))
btn_.on('mouseout', lambda:hover_out(btn_))

toggle = ToggleSwitch()
# toggle.checked(True)
root.add(toggle)

root.add(btn)
root.add(btn_)
root.add(Button(text='find', on_click=lambda:print(btn.get_style('backgroundColor'))))
root.add(Text(backgroundColor="steelblue",color="white", height="200px"))

root.add(radio1)
root.add(radio2)
root.add(radio3)



root.run()