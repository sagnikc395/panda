class TextNode:
    """
    text: text content of the node
    text_type: type of text this node contains, which is just a string like bold or italic
    url: URL of the link or iamge, if the text is a link. Default to None if nothing passed in
    """

    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def eq(self, other):
        return (
            True
            if (
                self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
            )
            else False
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    