from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, [], props)

  def to_html(self):
    if self.value is None:
      raise ValueError("LeafNode must have a value")
    if self.tag is None:
      return self.value
    else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
  
  def __eq__(self, value):
    return self.tag == value.tag and self.value == value.value and self.props == value.props

  def __repr__(self):
    return f"LeafNode({self.tag}, {self.value}, {self.props})"