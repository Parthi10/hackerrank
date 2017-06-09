#!/bin/python3

import sys
from collections import defaultdict
import re

q = int(input().strip())
file_list = defaultdict(int)
del_files =  defaultdict(list)

def create_file(file_name, print_flag):
    l = del_files[file_name]
    created_file = file_name
    if len(l) > 0:
        version = min(l)
        if print_flag:
            if version > 0:
                created_file = file_name + "(%s)" %version
                print("+ " + created_file)
            else: #version = 0
                print("+ " + created_file)
        del_files[file_name].remove(version)
    else:
        num = file_list[file_name]
        if num > 0:
            # print("num > 0")
            created_file = file_name + "(%s)" %num
            if print_flag:
                print("+ " + created_file)
        else:
            if print_flag:
                print("+ " + created_file)
        file_list[file_name] += 1
    # print(created_file, file_list)
    return created_file

def delete_file(file_name, print_flag):
    if "(" in file_name:
        version = int(re.search(r'\d+', file_name).group())
        if print_flag:
            print("- " + file_name)
        file_name = file_name.split("(")[0]
    else:
        version = 0
        if print_flag:
            print("- " + file_name)
    del_files[file_name].append(version)
    # print("del_files", del_files)

for a0 in range(q):
    command = input().strip().split(' ')
    comm = command[0]
    file_name = command[1]
    file_list[file_name]
    if comm == 'crt':
        create_file(file_name, True)

    elif comm == 'del':
        delete_file(file_name, True)

    else:
        new_name = command[2]
        delete_file(file_name, False)
        created_file = create_file(new_name, False)
        print("r " + file_name + " -> " + created_file)
