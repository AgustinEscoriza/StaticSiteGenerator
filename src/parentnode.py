from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)
    
  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode has no tag")
    if self.children is None or len(self.children) == 0:
      raise ValueError("Children has no value")
    return f"<{self.tag}{self.props_to_html()}>{''.join(list(map(lambda x: x.to_html(), self.children)))}</{self.tag}>"
  
  def __repr__(self):
    return f"ParentNode({self.tag}, children: {self.children}, {self.props})"