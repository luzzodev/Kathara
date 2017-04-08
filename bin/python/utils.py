import base64
import hashlib
import re
import os

def generate_urlsafe_hash(string):
    return base64.urlsafe_b64encode(hashlib.md5(string).digest())[:-2]

# helper functions for natural sorting
def atoi(text):
    return int(text) if text.isdigit() else text
def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def replace_multiple_items(repls, string):
        return reduce(lambda a, kv: a.replace(*kv), repls, string)

# writes the temporary files in NETKIT_HOME/temp
def write_temp(text, filename):
    out_file = open(os.path.join(os.environ["NETKIT_HOME"], "temp/" + filename),"w+")
    out_file.write(text)
    out_file.close()

def check_folder_or_file_name_in_dir(some_dir, file_or_folder_name):
    for dname, dirs, files in os.walk(some_dir):
        for directory_name in dirs:
            if (file_or_folder_name in directory_name): 
                return True
        for filename in files:
            if (file_or_folder_name in filename): 
                return True
