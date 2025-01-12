import unittest
from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_node_no_tag(self):
        # Test LeafNode with just a value
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_node_with_tag(self):
        # Test LeafNode with both tag and value
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_node_none_value(self):
        # Test that None value raises ValueError
        node = LeafNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_node_with_props(self):
        # Test LeafNode with properties
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.props["href"], "https://www.google.com")

    def test_leaf_node_empty_value(self):
        # Test LeafNode with empty string value
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

    def test_leaf_node_special_characters(self):
        # Test LeafNode with text containing special characters
        node = LeafNode("p", "Hello & goodbye!")
        self.assertEqual(node.to_html(), "<p>Hello & goodbye!</p>")


if __name__ == "__main__":
    unittest.main()
