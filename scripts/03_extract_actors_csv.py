#!/usr/bin/env python3
import csv
import ast

actors = set()

with open("data/credits.csv", "r") as infile, open("data/actors.csv", "w") as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["id", "name"])
    for line in reader:
        # Required because of non-standard format for json object
        movie_id = line["id"]
        cast = ast.literal_eval(line["cast"])
        for actor in cast:
            actor_id = actor["id"]
            if actor_id not in actors:
                writer.writerow([actor['id'], actor['name']])
                actors.add(actor_id)

