from enum import Enum
from leafnode import LeafNode
from parentnode import ParentNode


class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"


class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = TextType(text_type)
    self.url = url

  def __eq__(self, textnode):
    if self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url:
      return True
    return False
  
  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
  

def text_node_to_html_node(text_node):
  if text_node.text_type == TextType.TEXT:
    return LeafNode(tag=None, value=text_node.text)
  if text_node.text_type == TextType.BOLD:
    return LeafNode(tag="b", value=text_node.text)
  if text_node.text_type == TextType.ITALIC:
    return LeafNode(tag="i", value=text_node.text)
  if text_node.text_type == TextType.CODE:
    return LeafNode(tag="code", value=text_node.text)
  if text_node.text_type == TextType.LINK:
    return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
  if text_node.text_type == TextType.IMAGE:
    return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
  raise ValueError("TextType not valid")