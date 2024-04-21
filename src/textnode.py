from enum import Enum

from htmlnode import LeafNode


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

    def __eq__(self, other):
        if (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        ):
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


class NodeTypes(Enum):
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type not in NodeTypes:
        raise Exception("invalid text node type!!!")
    if text_node.text_type == NodeTypes.text_type_text:
        return LeafNode(text_node.text)
    if text_node.text_type == NodeTypes.text_type_bold:
        return LeafNode("b", text_node.text)
    if text_node.text_type == NodeTypes.text_type_italic:
        return LeafNode("i", text_node.text)
    if text_node.text_type == NodeTypes.text_type_code:
        return LeafNode("code", text_node.text)
    if text_node.text_type == NodeTypes.text_type_link:
        return LeafNode("a", text_node.text, text_node.url)
    if text_node.text_type == NodeTypes.text_type_image:
        return LeafNode("img", "", (text_node.url, text_node.text))

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    nodes = []
    for node in nodes:
        if node.text_type != NodeTypes.text_type_text:
            node.append(node)
        
        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError('Inavlid markdown, formatted sections are not closed')
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue 
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i],text_type=NodeTypes.text_type_text))
            else:
                split_nodes.append(TextNode(sections[i],text_type))

        nodes.extend(split_nodes)
    return nodes 