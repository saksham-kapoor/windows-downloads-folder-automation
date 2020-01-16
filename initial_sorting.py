import os
import shutil

path = "C:\\Users\\Saksham Kapoor\\Downloads"

file_list = os.listdir(path)


# os.path.splitext(file_) is used to split name of file and extenstion
os.mkdir(path + '\\Folders')
for file_ in file_list:
    name, ext = os.path.splitext(file_)

    ext = ext[1:]  # Removing '.' from extension

    if ext == '':
        shutil.move(path + '\\' + file_, path + '\\Folders' + '\\' + file_)
    elif os.path.exists(path+'\\'+ext):
        shutil.move(path + '\\' + file_, path + '\\' + ext + '\\' + file_)
    else:
        os.mkdir(path + '\\' + ext)
        shutil.move(path + '\\' + file_, path + '\\' + ext + '\\' + file_)
