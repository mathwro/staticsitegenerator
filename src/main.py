from textnode import TextNode, TextType

def main():
  new_textnode = TextNode("Hello, World!", TextType.PLAIN, "https://www.example.com")
  print(new_textnode)

if __name__ == "__main__":
  main()