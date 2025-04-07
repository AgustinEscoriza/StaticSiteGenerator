import os
import shutil

from copystatic import copy_files_recursive

dir_path_static = "./static"
dir_path_public = "./public"

def main():
  print("Deleting public dir...")
  if os.path.exists(dir_path_public):
    shutil.rmtree(dir_path_public)
  
  print("Copying static files to public dir...")
  copy_files_recursive(dir_path_static, dir_path_public)

main()