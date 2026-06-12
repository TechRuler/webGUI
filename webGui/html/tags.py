from webGui.html.container_tag import ContainerTag
from webGui.html.void_tag import VoidTag

class Textarea(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="textarea",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Div(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="div",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
        

class Span(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="span",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Section(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="section",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Article(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="article",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Header(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="header",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Footer(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="footer",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Main(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="main",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Nav(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="nav",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Aside(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="aside",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Form(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="form",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Label(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="label",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Button(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="button",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Fieldset(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="fieldset",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Ul(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="ul",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Ol(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="ol",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Li(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="li",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Table(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="table",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Thead(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="thead",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Tbody(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="tbody",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Tfoot(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="tfoot",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Tr(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="tr",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Td(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="td",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Th(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="th",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class A(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="a",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class P(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="p",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class H1(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h1",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class H2(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h2",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )



class H3(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h3",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class H4(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h4",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class H5(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h5",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class H6(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="h6",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class Strong(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="strong",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class B(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="b",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class I(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="i",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class Small(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="small",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class Code(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="code",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class Pre(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="pre",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Em(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="em",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )

class Canvas(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="canvas",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )


class Svg(ContainerTag):
    def __init__(self, attrs=None, children=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="svg",
            attrs=attrs,
            children=children,
            class_name=class_name,
            style=style,
            **kwargs
        )





class Input(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="input",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Img(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="img",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Br(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="br",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Hr(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="hr",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Meta(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="meta",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Link(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="link",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Source(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="source",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Track(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="track",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Area(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="area",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Col(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="col",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Embed(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="embed",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Param(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="param",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )
class Wbr(VoidTag):
    def __init__(self, attrs=None, class_name="", style=None, **kwargs):
        super().__init__(
            tag="wbr",
            attrs=attrs,
            class_name=class_name,
            style=style,
            **kwargs
        )