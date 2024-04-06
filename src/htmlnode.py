class HTMLNode:
    """
    tag -> string repr the HTML tag name
    value -> string repr that value of the HTML tag
    children -> list of HTMLNode object repr the children of the node
    props -> dict of kv pairs repr the attirbutes of the HTML tag.
    """

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    """
    should return a string that represents the HTML attributes of the node
    """

    def props_to_html(self):
        pass

    def __repr__(self):
        pass
