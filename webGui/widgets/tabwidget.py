from webGui.html.tags import Div, Span
from .label import Label


class Tab(Span):
    def __init__(self,frame, parent_widget, text, class_name=None, style=None, **kwargs):
        kwargs["default_style"] = {
            "display":"flex",
            "gap":"10px",
            "border":"1px solid black"
        }
        super().__init__(class_name=class_name, style=style, **kwargs)

        self.text = text 
        self.frame = frame 

        self.parent_widget = parent_widget

        self.label = Label(text=text)
        self.add(self.label)
    
    def closable(self):
        self.close = Label(text="x")
        self.add(self.close)
        self.close.on('click', self.closing)

    def closing(self):
        self.parent_widget.remove_tab(self)
    

class TabWidget(Div):
    def __init__(self, class_name=None, style=None, **kwargs):
        kwargs["default_style"] = {
            "padding":"10px"
        }
        super().__init__(class_name=class_name, style=style, **kwargs)

        self.tabs = []
        self.current_tab = None
        
        self.tab_bar = Div(default_style = {
            "display":"flex",
            "gap":"10px",
            "border":"1px solid black"
        })
        self.content = Div(default_style = {
            "border":"1px solid black"
        })

        self.add(self.tab_bar)
        self.add(self.content)

    def add_tab(self, frame, text):
        tab = Tab(parent_widget=self,frame=frame, text=text)

        frame.hide()
        self.content.add(frame)

        self.tab_bar.add(tab)
        self.tabs.append(tab)

        tab.on("click", lambda tab=tab: self.select(tab))
        tab.label.on("click", lambda tab=tab: self.select(tab))

        if len(self.tabs) == 1:
            self.select(tab)

        return tab

    def select(self, tab):
        if self.current_tab is tab:
            return

        if self.current_tab is not None:
            self.current_tab.frame.hide()
            self.current_tab.remove_class("active")

        self.current_tab = tab

        tab.frame.show()
        tab.add_class("active")
    
    def remove_tab(self, tab):
        tab.frame.remove()
        tab.remove()

        self.tabs.remove(tab)

        if self.current_tab is tab:
            self.current_tab = None

            if self.tabs:
                self.select(self.tabs[0])
    
    def get_current_tab(self):
        return self.current_tab
    
    def get_current_tab_frame(self):
        return self.current_tab.frame

    
    
    