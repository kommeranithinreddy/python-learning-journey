import os


print(os.getcwd())
dir_list = os.listdir()
for name in dir_list:
    print(name)