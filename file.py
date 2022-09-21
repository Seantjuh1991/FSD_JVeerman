__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil


#1
def clean_cache():
    dir = "file/cache"                                                              #line opzich niet nodig maar dit is netter dan overal "file/cache" typen.
    if not os.path.exists(dir):               
        return os.makedirs(dir)               
    for files in os.listdir(dir):           
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)


#2
def cache_zip(file, dir):
    clean_cache()                                                                   #was niet geheel duidelijk in de opdracht of deze function de map eerst ook moest legen. 
    shutil.unpack_archive(file, dir)


#3
def cached_files():
    path = os.path.abspath("file/cache")
    return [entry.path for entry in os.scandir(path) if entry.is_file()]


#4 Deze kan ongetwijfeld korter, maar hij werkt :)
def find_password(cached_files):
    for file in os.listdir("file/cache"):
        cur_path = os.path.join("file/cache", file)
        if os.path.isfile(cur_path):
            with open(cur_path, 'r') as file:
                if "password" in file.read():
                    with open(cur_path, 'r') as file:
                        for line in file:
                            if "password" in line:
                                password = line.rstrip()                           #Zonder de linebreak eruit te filteren pakte WINCPY hem niet. Dit duurde nog het langst om uit te vogelen :)
                                return password.split(" ")[1]

### TESTLINES ###
#clean_cache()
#cache_zip("file/data.zip", "file/cache")
#print(cached_files())
#print(find_password(cached_files()))



#minor bug in de nakijkcode: deze zoekt naar folder file ipv files. Folder hernoemt naar file.