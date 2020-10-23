import os
import json
import time


def count_letters(file, start, end, frequency):
    f = open(file, "r", encoding="utf8")
    f.seek(start)
    txt = f.read(end - start)
    for l in txt:
        letter = l.lower()
        if letter in frequency:
            frequency[letter] += 1


def main():
    frequency = {}
    for c in "abcdefghijklmnopqrstuvwxyz":
        frequency[c] = 0
    filename = "feedbacks.txt"
    size = os.stat(filename).st_size
    start = time.time()
    count_letters(filename, 0, size, frequency)
    end = time.time()
    print("Done, time taken", end - start)
    print(json.dumps(frequency, indent=4))


main()
