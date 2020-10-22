#!/usr/bin/env python3
import csv
import ast

with open("data/credits.csv", "r") as infile, open("data/movie_actors.csv", "w") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["movie_id", "actor_id"])
    for line in reader:
        # Required because of non-standard format for json object
        movie_id = line["id"]
        cast = ast.literal_eval(line["cast"])
        for actor in cast:
            writer.writerow([movie_id, actor["id"]])

