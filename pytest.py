#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os


# YOUR CODE GOES here

def main_function(directory):
    for directory in directories:
        if os.path.isdir(directory):
            search_and_print_node(directory)
        else:
            print("Directory " + directory + " doesn't exist!")
    return

def search_and_print_node(node, prefix=''):
    items = os.listdir(node)
    if len(items) == 0:
        return

    items.sort()
    key = 0
    currentPrefix = "├──"
    nextPrefix = "│  "
    while key < len(items):
        if key == len(items)-1:
            currentPrefix = "└──"
            nextPrefix = "   "
        print(prefix + currentPrefix + items[key])
        if os.path.isdir(os.path.join(node, items[key])):
            search_and_print_node(os.path.join(node, items[key]), nextPrefix)
        key+=1
    return

if __name__ == '__main__':
    # just for demo
    #subprocess.run(['tree'] + sys.argv[1:])
    if len(sys.argv) > 1:
        directories = sys.argv[1:]
    else:
        directories = ["."]

    main_function(directories)
