from webGui.config import state

class Menu:
    def __init__(self, app):
        self.app = app
    
    def get_window(self):
        """Helper to safely fetch the active window from context or parent app."""
        if self.app and self.app.window:
            return self.app.window
        if hasattr(state, 'ACTIVE_WINDOW') and state.ACTIVE_WINDOW:
            return state.ACTIVE_WINDOW
        return None

    def _execute_js(self, js):
        window = self.get_window()

        if window:
            return window.evaluate_js(js)

        state._PENDING_JS.append(js)
        return None
    
    def __check_id(self, menu):
        id = ""
        if menu == self.app:
            id = "menu-bar"
        else:
            id = menu.id 
    def add_menu(self, menu):
        pass

        


    
        