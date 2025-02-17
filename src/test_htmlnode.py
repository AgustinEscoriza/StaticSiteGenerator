import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_link(self):
    node = HTMLNode(
        tag="a",
        value="Click me!",
        props={"href": "https://www.google.com", "target": "_blank"}
    )
    expected = ' href="https://www.google.com" target="_blank"'
    self.assertEqual(node.props_to_html(), expected)

  def test_props_to_html_h1(self):
    node = HTMLNode(
        tag="h1",
        value="This is a heading",
        props={"class": "main-title"}
    )
    expected = ' class="main-title"'
    self.assertEqual(node.props_to_html(), expected)

  def test_props_to_html_p(self):
    node = HTMLNode(
        tag="p",
        value="This is a paragraph of text",
        props=None
    )
    expected = ''
    self.assertEqual(node.props_to_html(), expected)


if __name__ == "__main__":
  unittest.main()