import os
import re
from os.path import join

import time


def parse_to_array(text):
    taf = ".*TAF.*"
    comment = "\w*#.*"
    metar_close = ".*="
    lines = text.splitlines()
    metar_str = ""
    metars = []
    for line in lines:
        if re.search(taf, line):
            break
        if not re.search(comment, line):
            metar_str += line.strip()
        if re.search(metar_close, line):
            metars.append(metar_str)
            metar_str = ""
    return metars


def extract_wind_direction(metars):
    wind_regex = re.compile("\d* METAR.*EGLL \d*Z [A-Z ]*(\d{5}KT|VRB\d{2}KT).*=")
    winds = []
    for metar in metars:
        m = wind_regex.match(metar)
        if m:
            winds.append(m.group(1))
    return winds


def mine_wind_distribution(winds, wind_dist):
    variable_wind = re.compile(".*VRB\d{2}KT")
    valid_wind = re.compile("\d{5}KT")
    wind_dir_only = re.compile("(\d{3})\d{2}KT")
    for wind in winds:
        if variable_wind.match(wind):
            for i in range(8):
                wind_dist[i] += 1
        elif valid_wind.match(wind):
            d = int(wind_dir_only.match(wind).group(1))
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
