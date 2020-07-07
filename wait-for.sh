#!/bin/sh
# wait-for.sh

set -e
host="$1"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U $POSTGRES_USER -c '\q'; do
  >&2 echo "Postgres is unavailable"
  sleep 1
done

>&2 echo "Postgres is up!"
