import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
  def test_ParentNode(self):
    node = ParentNode(
      "p",
      [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
          LeafNode(None, "Normal text"),
      ],
    )
    expected = '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>'
    self.assertEqual(node.to_html(), expected)

  def test_ParentNode_empty_children(self):
    node = ParentNode("p", [])
    with self.assertRaises(ValueError):  # Expecting a ValueError for missing/empty children
        node.to_html()

  def test_nested_ParentNode(self):
    node = ParentNode(
        "div",
        [
            ParentNode("p", [LeafNode(None, "Nested text")]),
            LeafNode("i", "italic text"),
        ],
    )
    expected = '<div><p>Nested text</p><i>italic text</i></div>'
    self.assertEqual(node.to_html(), expected)

  def test_ParentNode_no_tag(self):
    with self.assertRaises(ValueError):  # Expecting a ValueError for missing tag
      ParentNode(None, [LeafNode("b", "Bold text")]).to_html()


  def test_ParentNode_with_props(self):
    node = ParentNode(
        "div",
        [LeafNode(None, "Hello!")],
        props={"class": "container", "id": "main"}
    )
    expected = '<div class="container" id="main">Hello!</div>'
    self.assertEqual(node.to_html(), expected)


  def test_ParentNode_single_child(self):
    node = ParentNode("span", [LeafNode(None, "Single child")])
    expected = '<span>Single child</span>'
    self.assertEqual(node.to_html(), expected)
  
  
if __name__ == "__main__":
  unittest.main()