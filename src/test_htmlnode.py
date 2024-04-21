import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(
            "div",
            "This is some div element",
            [
                HTMLNode("div", "Another child div inside", None, None),
                HTMLNode("a", "Google", None, {"href": "https://www.google.com"}),
            ],
            {"style": "border: 2px;padding: 2em;"},
        ).props_to_html()
        print(node)


class TestLeafNode(unittest.TestCase):
    def test_render_leafnode(self):
        node = LeafNode("p", "This is a paragraph of text.").to_html()
        print(node)
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        print(node2)


class TestParentNode(unittest.TestCase):
    def test_render_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ).to_html()
        print(node)


if __name__ == "__main__":
    unittest.main()
