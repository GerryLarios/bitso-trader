# bitso-trader

This app is an etrader coded with python, using the bitso api and setup with docker.

## Setup

Set the `env` file with your credentials

```bash
cp .env.sample .env
```

Write your credentials

```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=password
POSTGRES_DB=trade_development
HOST=database
PORT=5432
BITSO_API_KEY=123456789IDbitsoapi
BITSO_API_SECRET=123456789secretbitsoapi
```

## Run the app

User docker to setup the app

```bash
docker-compose up
```

if you need to check the database (Postgres) you can run the following app

```bash
docker-compose exec database bash
```
and then you have to enter into `psql`

```bash
psql --dbname=trade_development --user=postgres --host=database
```

## Final notes

DON'T USE THIS BOT TO TRADE! I'M NOT RESPONSABLE OF CASH LOSES!
