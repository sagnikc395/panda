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
        if self.props is None:
            return ""
        return " ".join([f'{key}="{value}"' for key, value in self.props.items()])

    def __repr__(self):
        return f"{self.tag} {self.value} {self.children} {self.props}"


class LeafNode(HTMLNode):
    """
    shouldnt allow for children
    the value data member is required.
    """

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    """
    to_html method should render a leaf node as a HTML string.
    if the leaf node has no value , it should then raise a ValueError.
    All leaf nodes would require a value.

    If tag is None, then the value should be returned as raw text.
    """

    def to_html(self):
        if not self.tag:
            return f"{self.value}"
        if not self.value:
            raise ValueError("All leaf nodes require a value")
        if not self.props:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag} {super().props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    """
    handle the nesting of HTML nodes inside of one another. Any HTML node that's not 'leaf' node (ie has children) is a parent node.
    """

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("parentnode tag not provided")
        if not self.children:
            raise ValueError("parentnode has no children present")
        
        """
        return a string repr of the HTML tag of the node and its children. should be a recusive method (with each recursion using a new node instance). 
        """
        html = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html
