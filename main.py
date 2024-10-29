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
exclude_file = input('name of the exclude file: ').strip()
# validate if the two directory path exists
if os.path.exists(strip_src_path) and os.path.exists(strip_dest_path):
    # save the listed files in a variable
    dir_list = os.listdir(strip_src_path)
    print("Files and directories in '", strip_src_path, "' :")
    print(dir_list)

    for file_name in dir_list:
        if file_name  == exclude_file:
            continue

        source = os.path.join(strip_src_path, file_name)

        destination = os.path.join(strip_dest_path, file_name)

        shutil.copy(source, destination)
        print('copied', file_name)

    path_save_zip = input('Where to save the zip: ').strip()


    # Creating the ZIP file
    archived = shutil.make_archive(path_save_zip, 'zip', strip_dest_path)

    if os.path.exists(path_save_zip + '.zip'):
        print(archived)
    else: 
        print("ZIP file not created")
else:
    print("One or both Directory paths not exists")




