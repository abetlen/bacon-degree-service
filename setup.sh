#!/bin/bash

echo "Unzipping archive.zip"
./scripts/00_unzip_archive.sh

echo "Extracting movies.csv"
./scripts/01_extract_movies_csv.py

echo "Extracting movie_actors.csv"
./scripts/02_extract_movie_actors_csv.py

echo "Extracting actors.csv"
./scripts/03_extract_actors_csv.py

echo "Initializing bacon.db"
./scripts/04_initialize_bacon_db.py

echo "Extracting actors_actors.csv edge list"
./scripts/05_extract_actors_actors_csv.py

echo "Pre-computing bacon degree table (may take a minute)"
./scripts/06_precompute_bacon_degree.py
