#!/usr/bin/env python3
import csv

with open("data/movies_metadata.csv", "r") as infile, open("data/movies.csv", "w"
) as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(["id", "title"])
    for line in reader:
        writer.writerow([line["id"], line["title"]])

