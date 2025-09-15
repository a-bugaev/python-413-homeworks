

```bash
#1
poetry install --no-root
#2
# create .env with valid values
#3
poetry run python ./manage.py migrate
#4
poetry run python ./manage.py throw_test_data
#5
poetry run python ./manage.py createsuperuser
#6
poetry run python ./manage.py runserver 9000
```