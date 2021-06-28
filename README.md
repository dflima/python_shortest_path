## Python Shortest Path

### Description

An JSON API made with Python+Django that searches for the shortest path in a graph

### Running the project

This repo uses Docker and docker-compose to setup the project locally.
To run the app:
```
docker compose up
```
This will build both the app and the database images

Then, to execute any python command (python shell, for example):
```
docker-compose run web python manage.py shell
```

## Endpoints

- POST /connectNode

```
{
  "from": <from_node in string format>
  "to": <to_node in string format>
}
```

- GET /path?from=<from_node>&to=<to_node>
```
{
  "Path": "A,B,C"
}
```
