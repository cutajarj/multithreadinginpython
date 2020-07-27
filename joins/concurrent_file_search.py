import os
from os.path import isdir, join
from threading import Lock, Thread

mutex = Lock()
matches = []


def file_search(root, filename):
    print("Searching in:", root)
    threads = []
    for file in os.listdir(root):
        full_path = join(root, file)
        if filename in file:
            mutex.acquire()
            matches.append(full_path)
            mutex.release()
        if isdir(full_path):
            t = Thread(target=file_search, args=([full_path, filename]))
            t.start()
            threads.append(t)
    for t in threads:
        t.join()


def main():
    t = Thread(target=file_search, args=(["c:/tools", "README.md"]))
    t.start()
    t.join()
    for m in matches:
        print("Matched:", m),


main()
