from textnode import TextNode, TextType
from copystatic import copy_files
from generate_page import generate_page
import os
import shutil

def main():
  new_textnode = TextNode("Hello, World!", TextType.TEXT, "https://www.example.com")
  print(new_textnode)
  dest = "public"
  src = "static"

  # Clear destination directory
  if os.path.exists(dest):
    if os.listdir(dest):
      # Delete files in destination directory
      for content in os.listdir(dest):
        content_path = os.path.join(dest, content)
        if os.path.isfile(content_path):
          os.remove(content_path)
        else:
          shutil.rmtree(content_path)

  copy_files(src, dest)
  print("Copy operation complete!")
  generate_page("content/index.html", "template.html", "public/index.html")

if __name__ == "__main__":
  main()