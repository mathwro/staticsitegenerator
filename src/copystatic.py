import os
import shutil


def copy_files(src, dest):
  # Recursive copy files from one directory to another
  if os.path.exists(dest):
    if os.listdir(dest):
      # Delete files in destination directory
      for content in os.listdir(dest):
        content_path = os.path.join(dest, content)
        if os.path.isfile(content_path):
          os.remove(content_path)
        else:
          shutil.rmtree(content_path)
  else:
    os.makedirs(dest)
    
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