import unittest

from htmlnode import HTMLNode


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
        )
        print(node)


if __name__ == "__main__":
    unittest.main()
