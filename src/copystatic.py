import os
import shutil


def copy_files(src, dest):
  os.makedirs(dest, exist_ok=True)  
  contents = os.listdir(src)
  for content in contents:
    src_path = os.path.join(src, content)
    dest_path = os.path.join(dest, content)
    print(f"Copying {src_path} to {dest_path}")
    if os.path.isdir(src_path):
      os.makedirs(dest_path, exist_ok=True)
      copy_files(src_path, dest_path)
    else:
      shutil.copy(src_path, dest_path)