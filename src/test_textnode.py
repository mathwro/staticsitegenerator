import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node1 = TextNode("Hello, World!", TextType.BOLD)
    node2 = TextNode("Hello, World!", TextType.BOLD)
    node3 = TextNode("Hello, World!", TextType.ITALIC)
    node4 = TextNode("Hello, World!", TextType.BOLD, None)
    self.assertEqual(node1, node2)
    self.assertNotEqual(node1, node3)
    self.assertEqual(node1, node4)




if __name__ == "__main__":
  unittest.main()