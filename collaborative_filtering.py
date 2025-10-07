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
import csv


def read_data(file_location):
    dataset = []
    with open(file_location, 'r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  
        for row in reader:
            user_id = int(row[0])
            movie_id = int(row[1])
            rating = float(row[2])
            timestamp = int(row[3]) # ignore for now
            dataset.append((user_id, movie_id, rating))
    print(f"Read {len(dataset)} entries from {file_location}")
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


recommendations = [
        (0, 12, 4.5),
        (1, 34, 3.9),
        (2, 56, 4.2),
        (3, 45, 3.8),
        (4, 75, 2.8),
        (5, 18, 4.9),
    ]



def output(recommendations):
    for pair_user_id, movie_id, predicted_rating in recommendations:
        print(f"{pair_user_id} {movie_id} {predicted_rating:.2f}")

def topN_output(n, recommendations):
    print("\nTop N recommendations")
    top = sorted(recommendations, key=lambda x: x[2], reverse=True)[:n]
    for user_id, movie_id, predicted_rating in top:
        print(f"{user_id} {movie_id} {predicted_rating}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collaborative_filtering.py <file_location> <similarity_threshold>")
        sys.exit(1)
    file_location = sys.argv[1]
    dataset = read_data(file_location)
    topN_output(3, recommendations)