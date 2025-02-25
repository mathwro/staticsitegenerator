from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("ParentNode must have a tag")
    if self.children is None:
      raise ValueError("ParentNode must have children")
    children_html = "".join([child.to_html() for child in self.children])
    return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

  def __eq__(self, other):
    return (
      self.tag == other.tag 
      and self.children == other.children 
      and self.props == other.props
    )

  def __repr__(self):
    return f"ParentNode({self.tag}, {self.children}, {self.props})"