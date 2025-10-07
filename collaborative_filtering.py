# Algorithms for Data Science -- Project

import urllib.request
import itertools
from itertools import combinations
import random
import math
import sys
from string import ascii_lowercase
from datetime import datetime
import numpy as np
import re
import string


def read_data(file_location):
    dataset = []
    with open(file_location, 'r', encoding='utf-8') as infile:
        for line in infile:
            dataset.append(str(line.strip()).lower())
    return dataset








if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python filtering.py <file_location> <similarity_threshold>")
        sys.exit(1)
    file_location = sys.argv[1]
    dataset = read_data(file_location)
    print(len(dataset))