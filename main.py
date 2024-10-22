import os
import shutil

src_path = input('set the source direcoty path: ')
dest_path = input('set the destiny directory path: ')

# remove spaces from the inputs 
stripped_src_path = src_path.strip()
strip_dest_path = dest_path.strip()

# input of the exclude path
exclude_file = input('name of the exclude file')
# validate if the two directory path exists
if os.path.exists(stripped_src_path and dest_path):
    # save the listed files in a variable
    dir_list = os.listdir(stripped_src_path)
    print("Files and directories in '", stripped_src_path, "' :")
    print(dir_list)

    path_save_zip = input('Where save the zip')

    strip_path_save_zip = path_save_zip.strip()
    # Creating the ZIP file
    archived = shutil.make_archive(stripped_src_path, 'zip', strip_path_save_zip)

    if os.path.exists(strip_path_save_zip):
        print(archived)
    else: 
        print("ZIP file not created")
else:
    print("Directory path not exists")




