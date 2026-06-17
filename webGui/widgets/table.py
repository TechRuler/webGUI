from webGui.html.tags import Table as html_table, Tr, Td, Th

class Row(Tr):
    def __init__(self, children=None, class_name="", style=None, **kwargs):
        kwargs["default_style"] = {
            "border":"1px solid black",
            "width":"max-content"
        }
        super().__init__(
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
    def add_heading(self, value):
        heading = Th(default_style = {
            "border":"1px solid black"
        })
        heading.innerText(value)
        self.add(heading)

    def add_data(self, value):
        data = Td(default_style = {
            "border":"1px solid black"
        })
        data.innerText(value)
        self.add(data)

class Table(html_table):
    def __init__(self, children=None, class_name="", style=None, **kwargs):
        kwargs["default_style"] = {
            "border": "1px solid black",
            "borderCollapse": "collapse",
            "width": "max-content"
        }
        super().__init__(
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

    def add_row(self, *values, row:Row=None):
        if row is not None:
            self.add(row)
            return row
        row = Row()

        for value in values:
            
            # data = Td()
            # row.add(data.innerText(value))
            row.add_data(value)

        self.add(row)
        return row

    def add_header(self, *values, row:Row=None):
        if row is not None:
            self.add(row)
            return row
        row = Row()

        for value in values:
            # header = Th()
            # row.add(header.innerText(value))
            row.add_heading(value)

        self.add(row)
        return row