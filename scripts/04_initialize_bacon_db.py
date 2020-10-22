#!/usr/bin/env python3
import csv
import sqlite3

conn = sqlite3.connect("bacon.db")
cursor = conn.cursor()

cursor.execute("create table if not exists actors(id text primary key, name text)")
cursor.execute("create table if not exists movies(id text primary key, title text)")
cursor.execute("create table if not exists movie_actors(movie_id text, actor_id text, primary key(movie_id, actor_id))")

with open("data/actors.csv", "r") as f:
    reader = csv.DictReader(f)
    cursor.executemany("insert or replace into actors(id, name) values (:id, :name)", reader)

with open("data/movies.csv", "r") as f:
    reader = csv.DictReader(f)
    cursor.executemany("insert or replace into movies(id, title) values (:id, :title)", reader)

with open("data/movie_actors.csv", "r") as f:
    reader = csv.DictReader(f)
    cursor.executemany("insert or replace into movie_actors(movie_id, actor_id) values (:movie_id, :actor_id)", reader)

conn.commit()
