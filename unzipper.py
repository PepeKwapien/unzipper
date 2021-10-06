from tkinter import filedialog
from tkinter import *
import os
import zipfile


def ask_for_directory():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    return folder_selected


def find_all_zips_in_directory(dir_path_from):
    zip_file_list = []
    if dir_path_from != '':
        zip_file_list = [os.path.join(dir_path_from, zip_file) for zip_file in os.listdir(dir_path_from) if zip_file.endswith(".zip")]
    return zip_file_list


def change_filename_into_directory(zip_file_path):
    return os.path.splitext(zip_file_path)[0]


def unzip_files_from_list(zip_file_list):
    for zip_file_path in zip_file_list:
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_to = change_filename_into_directory(zip_file_path)
            zip_ref.extractall(zip_to)
            print(zip_to.split("\\")[-1])


def delete_zip_files_from_list(zip_file_list):
    for zip_file_path in zip_file_list:
        os.remove(zip_file_path)


if __name__ == '__main__':
    file_list = find_all_zips_in_directory(ask_for_directory())
    unzip_files_from_list(file_list)
    delete_zip_files_from_list(file_list)
