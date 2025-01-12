class HTMLNode:
    """
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None or len(self.props) == 0:
            return ""

        props_strings = []
        for key, value in self.props.items():
            props_strings.append(f'{key}="{value}"')

        return " ".join(props_strings)

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"
