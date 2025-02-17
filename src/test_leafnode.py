import unittest

from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html_link(self):
    node = LeafNode(
      tag="a", 
      value="Click me!", 
      props={"href": "https://www.google.com"}
    )
    expected = '<a href="https://www.google.com">Click me!</a>'
    self.assertEqual(node.to_html(), expected)

  def test_props_to_html_h1(self):
    node = LeafNode(
        tag="h1",
        value="This is a heading",
        props={"class": "main-title"}
    )
    expected = '<h1 class="main-title">This is a heading</h1>'
    self.assertEqual(node.to_html(), expected)

  def test_props_to_html_p(self):
    node = LeafNode(
      tag="p",
      value="This is a paragraph of text."
    )
    expected = '<p>This is a paragraph of text.</p>'
    self.assertEqual(node.to_html(), expected)

  def test_to_html_no_tag(self):
    node = LeafNode(
        tag=None,
        value="Raw text with no wrapping tag."
    )
    expected = "Raw text with no wrapping tag."
    self.assertEqual(node.to_html(), expected)

  def test_to_html_no_value(self):
    with self.assertRaises(ValueError):
        node = LeafNode(tag="span", value=None)
        node.to_html()

  def test_no_children_allowed(self):
    with self.assertRaises(TypeError):  # Or a custom error if you've defined one
        LeafNode(tag="div", value="Nope", children=["Child node"])
        
if __name__ == "__main__":
  unittest.main()