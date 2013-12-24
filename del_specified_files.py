import os
import shutil

def get_target_directory():
    prompt = "Please input target directory: ";
    tar_dir = raw_input(prompt)
    if(verify_directory(tar_dir)):
        return tar_dir
    else:
        return get_target_directory()

def verify_directory(dir):
    if not os.access(dir, os.R_OK):
        print "Target directory [%s] doen't exist!" % dir
        return False;
    else:
        print "Target directory is [%s]" % dir
        return True;

def get_file_extentions():
    prompt = "Please input file types to del: ";
    ex_names = raw_input(prompt)

def get_folder_name():
    prompt = "Please input folder name to del: ";
    folder_name = ""
    while len(folder_name) == 0:
        folder_name = raw_input(prompt)
        
    return folder_name

def del_folders(parent, folder_name):
    for root,dirs,files in os.walk(parent):
        for d in dirs:
            if d == folder_name:
                shutil.rmtree(d)

tar_dir = get_target_directory()
folder_name = get_folder_name()
del_folders(tar_dir, folder_name)
