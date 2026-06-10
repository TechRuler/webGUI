from webGui.core.base import BaseWidget
import json

class Menu(BaseWidget):
    def __init__(self, class_name="", style=None, **kwargs):
        super().__init__(
            prefix="menu",
            on_event=None,
            event_suffix="select",
            class_name=class_name,
            style=style,
            **kwargs
        )

        # menu structure
        self.menus = {}

    # -----------------------------
    # Create top-level menu
    # -----------------------------
    def add_menu(self, label):
        if label not in self.menus:
            self.menus[label] = []

    # -----------------------------
    # Add item inside menu
    # -----------------------------
    def add_item(self, menu_label, item_label, function=None):
        if menu_label not in self.menus:
            self.menus[menu_label] = []

        self.menus[menu_label].append((item_label, function))

    # -----------------------------
    # Render UI
    # -----------------------------
    def render(self):
        window = self.get_window()
        if not window:
            return

        data = {
            menu: [item[0] for item in items]
            for menu, items in self.menus.items()
        }

        style_json = json.dumps(self.style or {})
        data_json = json.dumps(data)
        parent_target = getattr(self, "_target_parent_id", "menubar")

        js = f"""
        (function(){{
            const bar = document.createElement("div");
            bar.id = "{self.id}";
            Object.assign(bar.style, {style_json});

            bar.style.display = "flex";
            bar.style.gap = "15px";
            bar.style.alignItems = "center";
            bar.style.height = "100%";

            const data = {data_json};

            Object.keys(data).forEach(menuName => {{
                const menu = document.createElement("div");
                menu.innerText = menuName;
                menu.style.position = "relative";
                menu.style.cursor = "pointer";
                menu.style.padding = "6px 10px";

                const dropdown = document.createElement("div");
                dropdown.style.position = "absolute";
                dropdown.style.top = "100%";
                dropdown.style.left = "0";
                dropdown.style.background = "#2b2b2b";
                dropdown.style.display = "none";
                dropdown.style.flexDirection = "column";
                dropdown.style.minWidth = "140px";
                dropdown.style.zIndex = "9999";

                data[menuName].forEach(item => {{
                    const el = document.createElement("div");
                    el.innerText = item;
                    el.style.padding = "8px";
                    el.style.cursor = "pointer";
                    el.style.color = "white";

                    el.onclick = () => {{
                        window.pywebview.api.trigger_event(
                            "{self.id}",
                            "select",
                            menuName + ":" + item
                        );
                    }};

                    dropdown.appendChild(el);
                }});

                menu.appendChild(dropdown);

                menu.onmouseenter = () => {{
                    dropdown.style.display = "flex";
                }};

                menu.onmouseleave = () => {{
                    dropdown.style.display = "none";
                }};

                bar.appendChild(menu);
            }});

            const parent = document.getElementById(menubar);
            if (parent) parent.appendChild(bar);
        }})();
        """

        window.evaluate_js(js)