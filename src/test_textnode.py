import unittest

from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)
  
  def test_not_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is another text", TextType.CODE)
    self.assertNotEqual(node, node2)

  def test_dist_text(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is another text", TextType.BOLD)
    self.assertNotEqual(node, node2)

  def test_dist_textType(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.ITALIC)
    self.assertNotEqual(node, node2)

  def test_text_node_to_html_node(self):
    # Test regular text
    text_node = TextNode("Hello, world!", TextType.TEXT)
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag is None
    assert html_node.value == "Hello, world!"
    assert html_node.props == None

    # Test bold text
    text_node = TextNode("Bold text", TextType.BOLD)
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag == "b"
    assert html_node.value == "Bold text"

    
    # Test italic text
    text_node = TextNode("Italic text", "italic")
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag == "i"
    assert html_node.value == "Italic text"
    assert html_node.props == None

    # Test code text
    text_node = TextNode("Code text", "code")
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag == "code"
    assert html_node.value == "Code text"
    assert html_node.props == None

    # Test link
    text_node = TextNode("Click me", "link", "https://www.boot.dev")
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag == "a"
    assert html_node.value == "Click me"
    assert html_node.props == {"href": "https://www.boot.dev"}

    # Test image
    text_node = TextNode("Alt text", "image", "https://i.imgur.com/123.png")
    html_node = text_node_to_html_node(text_node)
    assert html_node.tag == "img"
    assert html_node.value == ""
    assert html_node.props == {
      "src": "https://i.imgur.com/123.png",
      "alt": "Alt text"
    }
if __name__ == "__main__":
  unittest.main()