# from webGui import App 

# from webGui.widgets import Text, Button, RadioButton, ToggleSwitch, ComboBox, ListBox

# root = App(title="App", width=800, height=600)

# def hover_in(btn):
#     btn.filter("brightness(90%)")
# def hover_out(btn):
#     btn.filter("brightness(100%)")


# btn = Button(padding="20px", backgroundColor="red", fontSize="20px", width='max-content')
# btn.textContent(text="he")
# btn_ = Button(text='he',on_click=lambda:btn.set_style("backgroundColor","blue"),padding="20px", backgroundColor="red", fontSize="20px", width='max-content')
# # btn_.textContent(text="he")

# radio1 = RadioButton(text="Male", group='gender')
# radio2 = RadioButton(text="Female", group='gender')
# radio3 = RadioButton(text="Other", group='gender')

# btn.on('mouseover', lambda:hover_in(btn))
# btn.on('mouseout', lambda:hover_out(btn))
# btn_.on('mouseover', lambda:hover_in(btn_))
# btn_.on('mouseout', lambda:hover_out(btn_))

# toggle = ToggleSwitch()
# # toggle.checked(True)
# root.add(toggle)
# toggle.active('red')


# comobox = ComboBox(options=["python","c++"], width='max-content')

# root.add(comobox)

# listbox = ListBox(padding="5px", border="1px solid black", width='max-content', margin='5px')

# listbox.add_item("code")
# listbox.add_item("code")
# listbox.add_item("code")
# listbox.add_item("code")

# root.add(listbox)
# root.add(btn)
# root.add(btn_)
# # root.add(Button(text='find', on_click=lambda:print(btn.get_style('backgroundColor'))))
# root.add(Button(text='find', on_click=lambda:print(btn.innerText())))
# root.add(Text(backgroundColor="steelblue",color="white", height="200px"))

# root.add(radio1)
# root.add(radio2)
# root.add(radio3)



# root.run()


import webview
from webGui import App
from webGui.widgets import Table, Row

root = App(
    title="Closable Tabs Demo",
    width=800,
    height=600
)
table = Table(
    border="1px solid black",
    borderCollapse="collapse"
)

table.add_header("Name", "Age", "City")

table.add_row("Anmol", 18, "Delhi")
table.add_row("John", 25, "London")

root.add(table)

table = Table()

header = Row()
header.add_heading("Name")
header.add_heading("Age")
header.add_heading("City")

table.add_header(row=header)

row = Row()
row.add_data("Anmol")
row.add_data("18")
row.add_data("Delhi")

table.add_row(row=row)

root.add(table)

root.run(menu= [
    root.Menu(
        'File',
        [
            root.MenuAction('Open', lambda: print('Open')),
            root.MenuAction('Exit', lambda:print("edit"))
        ]
    ),
    
])