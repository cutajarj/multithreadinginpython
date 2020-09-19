import os
from os.path import isdir, join
from threading import Lock, Thread

from conditionVariables.wait_group import WaitGroup

mutex = Lock()
matches = []


def file_search(root, filename, wait_group):
    print("Searching in:", root)
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            wait_group.add(1)
            t = Thread(target=file_search, args=([full_path, filename, wait_group]))
            t.start()
    wait_group.done()


def main():
    wait_group = WaitGroup()
    wait_group.add(1)
    t = Thread(target=file_search, args=(["c:/tools", "README.md", wait_group]))
    t.start()
    wait_group.wait()
    for m in matches:
        print("Matched:", m)


main()
