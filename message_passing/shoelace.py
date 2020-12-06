import re
from multiprocessing import Process, Queue

import time

PTS_REGEX = "\((\d*),(\d*)\)"
TOTAL_PROCESSES = 8


def find_area(points_queue):
    points_str = points_queue.get()
    while points_str is not None:
        points = []
        area = 0.0
        for xy in re.finditer(PTS_REGEX, points_str):
            points.append((int(xy.group(1)), int(xy.group(2))))

        for i in range(len(points)):
            a, b = points[i], points[(i + 1) % len(points)]
            area += a[0] * b[1] - a[1] * b[0]

#       print(abs(area) / 2.0)
        points_str = points_queue.get()


if __name__ == "__main__":
    queue = Queue()
    processes = []
    for i in range(TOTAL_PROCESSES):
        p = Process(target=find_area, args=(queue,))
        processes.append(p)
        p.start()
    f = open("polygons.txt", "r")
    text = f.read()
    lines = text.splitlines()
    start = time.time()
    for line in lines:
        queue.put(line)
    for i in range(TOTAL_PROCESSES): queue.put(None)
    for i in range(TOTAL_PROCESSES): processes[i].join()
    end = time.time()
    print("Time taken", end - start)
