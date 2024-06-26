# GLFC Technical Aptitude Evaluation
Mark Guiang
## Prerequisites
- Docker
- Python >= 3.8, run these **ONLY** if you want to run test/dev build
  - ```$ python -m venv env```
  - ```$ source env/bin/activate```
  - ```$ python -m pip install -r ./loanflask/requirements.txt```
  - ```$ docker compose -f compose-db-only.yaml up --detach```

## How to run
### Production Build
```$ docker compose up --detach``` would run and expose app on localhost:80
### Dev Build
```$ python wsgi.py``` on localhost:5000
### Test
```$ python -m pytest ./tests```


## API Information
- Method: POST
- Request Body (JSON):
  - ```name```
  - ```amount```: The desired loan amount. Min:```1000```, Max:```10000```.
  - ```term```: The loan term. Possible values: ```[3,6,9,12,15,18]```
- Response Body (JSON):
  - ```Principal Loan Amount```
  - ```Monthly Payment Amount```
  - ```Total Interest Amount```
  - ```Loan Term```
  - ```Total Sum of Payments```
 
## How to use
- Example Request
  ```
  $ curl -X POST \
    -H "Content-Type: application/json" \
    -d '{"name":"mark","amount":"10000","term":"12"}' \
    http://localhost:80/loan
  ```
- Export data to out.tsv
  ```
  $ docker compose exec db bash -c "MYSQL_PWD=\$(cat /run/secrets/db_pass) mysql -u root --database task --batch \
    -e 'select users.name, loans.amount, loans.term from users inner join loans on users.id = loans.user_id'" > out.tsv
  ```


## Notes 
  - mysql root password for production is in ```secrets/db_pass.txt``` hehe, dont actually include it in version control
