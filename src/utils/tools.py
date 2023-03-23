import os

def get_temp_path(file_path):
    temp_file_name = 'temp_' + os.path.basename(file_path)
    return os.path.join(os.path.dirname(file_path), temp_file_name)

def remove_file (file_path):
    os.remove(file_path)