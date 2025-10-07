# Algorithms for Data Science -- Project

import sys
import csv
from collections import defaultdict

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
    user_ratings = defaultdict(dict)  
    for user_id, movie_id, rating in dataset:
        user_ratings[user_id][movie_id] = rating
    return user_ratings

def collaborative_filtering():
    print("Collaborative filtering algorithm")


def finding_neighbors():
    print("Finding neighbors algorithm")
    print("first shingling")
    print("then minhashing")
    print("then LSH")
    common_movies = set(user1.keys()) & set(user2.keys())
    if not common_movies:
        return 0
    num = sum(user1[m]*user2[m] for m in common_movies)
    den1 = sum(user1[m]**2 for m in common_movies)**0.5
    den2 = sum(user2[m]**2 for m in common_movies)**0.5
    return num / (den1*den2) if den1 and den2 else 0

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