#!/bin/sh

echo "Waiting for mysql..."

while ! nc -z 0.0.0.0 3306; do
  sleep 0.5
  echo "wait..."
done

echo "Mysql started"


sleep 5
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000

exec "$@"
