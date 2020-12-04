import os
import re
from os.path import join

import time

WIND_REGEX = re.compile("\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*=")
VARIABLE_WIND_REGEX = re.compile(".*VRB\d{2}KT")
VALID_WIND_REGEX = re.compile("\d{5}KT")
WIND_DIR_ONLY_REGEX = re.compile("(\d{3})\d{2}KT")
TAF_REGEX = re.compile(".*TAF.*")
COMMENT_REGEX = re.compile("\w*#.*")
METAR_CLOSE_REGEX = re.compile(".*=")


def parse_to_array(text):
    lines = text.splitlines()
    metar_str = ""
    metars = []
    for line in lines:
        if TAF_REGEX.search(line):
            break
        if not COMMENT_REGEX.search(line):
            metar_str += line.strip()
        if METAR_CLOSE_REGEX.search(line):
            metars.append(metar_str)
            metar_str = ""
    return metars


def extract_wind_direction(metars):
    winds = []
    for metar in metars:
        m = WIND_REGEX.match(metar)
        if m:
            winds.append(m.group(1))
    return winds


def mine_wind_distribution(winds, wind_dist):
    for wind in winds:
        if VARIABLE_WIND_REGEX.match(wind):
            for i in range(8):
                wind_dist[i] += 1
        elif VALID_WIND_REGEX.match(wind):
            d = int(WIND_DIR_ONLY_REGEX.match(wind).group(1))
            dir_index = round(d / 45.0) % 8
            wind_dist[dir_index] += 1
    return wind_dist


if __name__ == "__main__":
    path_with_files = "../metarfiles"
    wind_dist = [0] * 8
    start = time.time()
    for file in os.listdir(path_with_files):
        f = open(join(path_with_files, file), "r")
        text = f.read()
        metars = parse_to_array(text)
        winds = extract_wind_direction(metars)
        wind_dist = mine_wind_distribution(winds, wind_dist)
    end = time.time()
    print(wind_dist)
    print("Time taken", end - start)
