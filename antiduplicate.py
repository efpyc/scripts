# -*- coding:utf-8 -*-

# This tool for removing duplicate items on the .txt file.

import os
import datetime

__author__ = "efpyc"
temp = 0


def get_filename(old_file_name : str):
    return datetime.datetime.now().strftime(f"{old_file_name.strip('.txt')} %H.%M.%S %d-%m-%Y.txt")

def remove_duplicates(fpath):
    global temp
    cleaned = list()
    file_name = fpath.split(os.sep)[-1]
    with open(fpath, "r", encoding="utf-8") as old_file:
        content = old_file.readlines()
        for y in content:
            if not y in cleaned:
                cleaned.append(y)
    with open(os.path.join(fpath.strip(file_name), get_filename(file_name)), "w", encoding="utf-8") as new_file:
        for x in cleaned:
            temp += 1
            new_file.write(x)
            print(f"[{temp}] {x}", end="")

if __name__ == '__main__':
    print(r"""
   _____            __   .__  
  /  _  \    ____ _/  |_ |__| 
 /  /_\  \  /    \\   __\|  | 
/    |    \|   |  \|  |  |  | 
\____|__  /|___|  /|__|  |__| 
        \/      \/            
                              
________                  .__   .__                  __            
\______ \   __ __ ______  |  |  |__|  ____  _____  _/  |_   ____   
 |    |  \ |  |  \\____ \ |  |  |  |_/ ___\ \__  \ \   __\_/ __ \  
 |    `   \|  |  /|  |_> >|  |__|  |\  \___  / __ \_|  |  \  ___/  
/_______  /|____/ |   __/ |____/|__| \___  >(____  /|__|   \___  > 
        \/        |__|                   \/      \/            \/  

https://github.com/efpyc/
    """)

    ask_file = input("[?] File Path: ")
    print("\n", end="")
    remove_duplicates(ask_file)