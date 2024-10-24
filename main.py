import os
import shutil

# source path
src_path = input('set the source direcoty path: ')
# destiny path
dest_path = input('set the destiny directory path: ')

# remove spaces from the inputs 
strip_src_path = src_path.strip()
strip_dest_path = dest_path.strip()

# input of the exclude path
exclude_file = input('name of the exclude file')
# validate if the two directory path exists
if os.path.exists(strip_src_path and strip_dest_path):
    # save the listed files in a variable
    dir_list = os.listdir(strip_src_path)
    print("Files and directories in '", strip_src_path, "' :")
    print(dir_list)

    for file_name in dir_list:
        source = strip_dest_path + file_name

        destination = strip_dest_path + file_name

        shutil.copy(source, destination)
        print('copied', file_name)

    path_save_zip = input('Where save the zip: ')

    strip_path_save_zip = path_save_zip.strip()
    # Creating the ZIP file
    archived = shutil.make_archive(strip_dest_path, 'zip', strip_path_save_zip)

    if os.path.exists(strip_path_save_zip):
        print(archived)
    else: 
        print("ZIP file not created")
else:
    print("Directory path not exists")




