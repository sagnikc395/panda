import unittest

from htmlnode import HTMLNode, LeafNode


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
        node = LeafNode("This is a paragraph of text.", "p").to_html()
        print(node)
        node2 = LeafNode("Click me!", "a", {"href": "https://www.google.com"}).to_html()
        print(node2)


if __name__ == "__main__":
    unittest.main()
