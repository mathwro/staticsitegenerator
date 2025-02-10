import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def test_eq(self):
    node1 = HTMLNode("div", "Hello, World!", [], {"id": "main"})
    node2 = HTMLNode("div", "Hello, World!", [], {"id": "main"})
    node3 = HTMLNode("h1", "Hello, World!", [], {"id": "main"})
    node4 = HTMLNode("div", "Hello, World!", [], {"id": "main"})
        
    self.assertEqual(node1, node2)
    self.assertNotEqual(node1, node3)
    self.assertEqual(node1, node4)

  def test_props_to_html(self):
    node = HTMLNode("div", "Hello, World!", [], {"id": "main", "class": "container"})
    self.assertEqual(node.props_to_html(), ' id="main" class="container"')
  
    node_no_props = HTMLNode("div", "Hello, World!")
    self.assertEqual(node_no_props.props_to_html(), "")

if __name__ == "__main__":
  unittest.main()