class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props is None:
      return ""
    result = ""
    for prop in self.props:
      props_html += f' {prop}="{self.props[prop]}"'
    return result
  
  def __eq__(self, other):
    return (
        self.tag == other.tag
        and self.value == other.value
        and self.children == other.children
        and self.props == other.props
    )

  def __repr__(self):
    print = f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, None, props)

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