import os
from os.path import isdir, join

matches = []


def file_search(root, filename):
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            matches.append(full_path)
        if isdir(full_path):
            file_search(full_path, filename)


def main():
    file_search("c:/tools", "README.md")
    for m in matches:
        print("Matched:", m),


main()
