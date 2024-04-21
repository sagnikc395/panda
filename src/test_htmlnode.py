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

    def test_props_to_html(self):
        htmlnode = HTMLNode(
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        html = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(htmlnode.props_to_html(), html)

    def test_render_leafnode(self):
        tests = {
            LeafNode(
                "p", "This is a paragraph of text."
            ).to_html(): "<p>This is a paragraph of text.</p>",
            LeafNode(
                "a", "Click me!", {"href": "https://www.google.com"}
            ).to_html(): '<a href="https://www.google.com">Click me!</a>',
        }
        for test in tests.items():
            self.assertEqual(test[0], test[1])

    def test_render_parent_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )


if __name__ == "__main__":
    unittest.main()
