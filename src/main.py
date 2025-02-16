from textnode import TextNode, TextType
from copystatic import copy_files

def main():
  new_textnode = TextNode("Hello, World!", TextType.TEXT, "https://www.example.com")
  print(new_textnode)
  copy_files("static", "public")
  print("Copy operation complete!")  

if __name__ == "__main__":
  main()