# Bacon Degree Service

HTTP web service to return the [Bacon Number](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) for any actor in [The Movie Dataset]().

## Setup

First download the dataset [here](https://www.kaggle.com/rounakbanik/the-movies-dataset) and place the `archive.zip` file into the `data` directory.

```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
# Initialize bacon.db from movies dataset and precompute bacon degree table
$ ./setup.sh
# Run tests
$ python -m unittest
# Run gunicorn server on port 5050
$ PORT=5050 ./run.sh
```

or to run in docker

```bash
$ docker build -t bacon .
$ docker run \
  -d \
  --rm \
  -v $(pwd)/bacon.db:/data/bacon.db \
  -p 5000:5000 \
  bacon
```

## API

```
GET /actors/search/bacon-degree?name=<name>
```

Get bacon degree of actor(s) by name.


```
GET /actors/search?name=<name>
````

Get actor ids by name.

```
GET /actors/<actor_id>/movies
```

Get actor movies.

```
GET /actors/<actor_id>/bacon-degree
```

 Get actor bacon degree.
