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

def preprocess_data(dataset):
    print("Preprocessing data")

def collaborative_filtering():
    print("Collaborative filtering algorithm")

def finding_neighbors():
    print("Finding neighbors algorithm")
    print("first shingling")
    print("then minhashing")
    print("then LSH")

def similarity_computation():
    print("Similarity computation algorithm")

def predict_ratings():
    print("Predict ratings algorithm")

def output():
    print("top 5 recommendations")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collaborative_filtering.py <file_location> <similarity_threshold>")
        sys.exit(1)
    file_location = sys.argv[1]
    dataset = read_data(file_location)
    print(len(dataset))