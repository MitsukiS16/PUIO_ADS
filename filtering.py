# Algorithms for Data Science -- Project

import urllib.request
import itertools
from itertools import combinations
import random
import math
from string import ascii_lowercase
from datetime import datetime
import sys
import numpy as np
import urllib.request
import re
import string
import random

def read_data():
    file_location = 'train_ratings.csv'
    dataset = []
    with open(file_location, 'r', encoding='utf-8') as infile:
        for line in infile:
            dataset.append(str(line.strip()).lower())
    return dataset

dataset = read_data()
print(len(dataset))
