#!/usr/bin/env python3
import csv
import sqlite3

conn = sqlite3.connect("bacon.db")
cursor = conn.cursor()

rows = cursor.execute("""
select distinct a.actor_id, b.actor_id 
from movie_actors a, movie_actors b
where a.movie_id = b.movie_id and a.actor_id <> b.actor_id
""")

with open("data/actors_actors.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerows(rows)

