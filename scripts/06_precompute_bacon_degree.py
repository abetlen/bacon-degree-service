#!/usr/bin/env python3
import csv
import sqlite3
import networkx as nx

conn = sqlite3.connect("bacon.db")
cursor = conn.cursor()

cursor.execute("create table if not exists bacon_degree(id text primary key, degree integer)")

rows = cursor.execute("select id from actors where name = :name", { "name": "Kevin Bacon" })
bacon_id, = rows.fetchone()

g = nx.read_edgelist("data/actors_actors.csv", delimiter=",")

length = nx.single_source_shortest_path_length(g, bacon_id)

cursor.executemany("insert or replace into bacon_degree(id, degree) values (?, ?)", length.items())

conn.commit()
