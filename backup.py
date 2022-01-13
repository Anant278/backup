import time
import os
import shutil

path = input("Enter the file path: ")

days = input(int("Enter number of days: "))
secs = time.time(days)

if os.path.exists(path):
    os.walk(path)
    file_path = input("Enter file/folder path: ")
    ctime = os.stat(path).st_ctime
    if ctime > secs:
        shutil.rmtree(path)
else:
    print("Path not found")