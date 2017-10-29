import os


def renameFile():
    # get thefile names
    original_path = os.getcwd()
    print(original_path)
    os.chdir(original_path + "\prank")
    file_list = os.listdir(original_path + "\prank")
    print(file_list)
    # for each file, rename the file
    for file in file_list:
        print(file)
        try:
            print("renaming file: " +   file)
            os.rename(file,file.translate(None,"0123456789"))

        except:
            print("Error renaming the file")
 

    


renameFile()
