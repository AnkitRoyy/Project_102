import os
import shutil

from_dir = "C:/Users/Office/Documents/File sorter"
to_dir = "C:/Users/Office/Desktop/Project 102 - File sorter"

dir_listing = os.listdir("C:/Users/Office/Documents/File sorter")

for files in dir_listing:

    name, ext = os.path.splitext(files)

    if ext == '':
        continue

    if ext in ['.xlsx', '.pdf', '.txt', '.doc', '.docx']:

        path1 = from_dir+'/'+files
        path2 = to_dir+'/'+'document_files'
        path3 = to_dir+'/document_files/'+files

        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            shutil.move(path1, path3)