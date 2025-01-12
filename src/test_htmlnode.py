import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty(self):
        # Test with empty props
        node = HTMLNode("div", "Hello", None, {})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        # Test with a single property
        node = HTMLNode("a", "Click me!", None, {"href": "https://www.google.com"})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com"')

    def test_props_to_html_multiple_props(self):
        # Test with multiple properties
        node = HTMLNode(
            "img", "", None, {"src": "test.jpg", "alt": "Test image", "width": "100"}
        )
        # Note: Since dictionaries are unordered, we need to check for all combinations
        # or split and check parts independently
        result = node.props_to_html()
        self.assertIn('src="test.jpg"', result)
        self.assertIn('alt="Test image"', result)
        self.assertIn('width="100"', result)

    def test_node_creation_no_props(self):
        # Test creating a node without props
        node = HTMLNode("p", "Hello, world!")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello, world!")
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_node_creation_with_children(self):
        # Test creating a node with children
        child = HTMLNode("span", "child text")
        parent = HTMLNode("div", "parent text", [child])
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0].value, "child text")


if __name__ == "__main__":
    unittest.main()
