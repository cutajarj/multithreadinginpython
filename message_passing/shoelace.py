import re
import time

PTS_REGEX = "\((\d*),(\d*)\)"


def find_area(points_str):
    points = []
    area = 0.0
    for xy in re.finditer(PTS_REGEX, points_str):
        points.append((int(xy.group(1)), int(xy.group(2))))

    for i in range(len(points)):
        a, b = points[i], points[(i + 1) % len(points)]
        area += a[0] * b[1] - a[1] * b[0]

#    print(abs(area) / 2.0)


f = open("polygons.txt", "r")
text = f.read()
lines = text.splitlines()
start = time.time()
for line in lines:
    find_area(line)
end = time.time()
print("Time taken", end - start)