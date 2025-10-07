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


# def finding_neighbors():
#     print("Finding neighbors algorithm")
#     print("first shingling")
#     print("then minhashing")
#     print("then LSH")


#def similarity_computation():
#    print("Similarity computation algorithm")

def predict_ratings(user_id, movie_id, user_ratings):
    total = 0
    count = 0
    for ratings in user_ratings.values():
        if movie_id in ratings:
            total += ratings[movie_id]
            count += 1
    if count == 0:
        return 0
    return total / count


def collaborative_filtering(user_ratings, all_movie_ids):
    recommendations = []
    for user_id in user_ratings:
        for movie_id in all_movie_ids:
            if movie_id not in user_ratings[user_id]:
                rating = predict_ratings(user_id, movie_id, user_ratings)
                if rating > 0:
                    recommendations.append((user_id, movie_id, rating))
    return recommendations


def topN_output(n, recommendations):
    top = sorted(recommendations, key=lambda x: x[2], reverse=True)[:n]
    for user_id, movie_id, predicted_rating in top:
        print(f"User {user_id} -> Movie {movie_id} : {predicted_rating:.2f}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collaborative_filtering.py <file_location> <similarity_threshold>")
        sys.exit(1)

    file_location = sys.argv[1]
    dataset = read_data(file_location)
    user_ratings = preprocess_data(dataset)
    all_movie_ids = set(movie_id for _, movie_id, _ in dataset)

    print("Predicting ratings, please wait...")
    recommendations = collaborative_filtering(user_ratings, all_movie_ids)  
    topN_output(10, recommendations)