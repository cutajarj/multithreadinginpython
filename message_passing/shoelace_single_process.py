import re
import time
# (45,11),(41,15),(36,20)

PTS_REGEX = "\((\d*),(\d*)\)"


def find_area(points_str):
    points = []
    area = 0.0
    for xy in re.finditer(PTS_REGEX, points_str):
        points.append((int(xy.group(1)), int(xy.group(2))))

    for i in range(len(points)):
        a, b = points[i], points[(i + 1) % len(points)]
        area += a[0] * b[1] - a[1] * b[0]
    area = abs(area) / 2.0
    # print(area)


f = open("polygons.txt", "r")
lines = f.read().splitlines()
start = time.time()
for line in lines:
    find_area(line)
end = time.time()
print("Time taken", end - start)
