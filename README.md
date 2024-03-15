# GLFC Technical Aptitude Evaluation
Mark Guiang
## Prerequisites
- Docker
- Python >= 3.8, **ONLY** if you want to run test/dev build
  - <code>$ python -m pip install -r ./loanflask/requirements.txt</code>
  - ```$ docker compose -f compose-db-only.yaml up```

## How to run
### Production Build
```$ docker compose up``` would run and expose app on localhost:80
### Dev Build
```$ python wsgi.py``` on localhost:5000
### Test
```$ python -m pytest /tests```
## How to use
```
$ curl -X POST \
-H "Content-Type: application/json" \
-d '{"name":"mark","amount":"10000""term":"12"}' \
http://localhost:80/loan
```
