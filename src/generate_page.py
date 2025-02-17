from inline_markdown import extract_title
from markdown_blocks import markdown_to_html_node
import os

def generate_page(from_path, template_path, dest_path):
  print(f"Generating page from {from_path} to {dest_path} using {template_path}")
  with open(from_path, "r") as f:
    content_from = f.read()
  with open(template_path, "r") as f:
    template = f.read()
    
  html = markdown_to_html_node(content_from).to_html()
  title = extract_title(content_from)
  html = template.replace("{{ Title }}", title).replace("{{ Content }}", html)
  if not os.path.exists(os.path.dirname(dest_path)):
    os.makedirs(os.path.dirname(dest_path))
  with open(dest_path, "w") as f:
    f.write(html)
    
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
  contents = os.listdir(dir_path_content)
  for content in contents:
    src_path = os.path.join(dir_path_content, content)
    if os.path.isdir(src_path):
      generate_pages_recursive(src_path, template_path, os.path.join(dest_dir_path, content))
    else:
      if content.endswith(".md"):
        generate_page(src_path, template_path, os.path.join(dest_dir_path, content.replace(".md", ".html")))