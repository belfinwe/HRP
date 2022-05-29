# TODO

1. Figure out a proper `docker-compose.yml`.
2. Figure out proper relation between tables in SQLAlchemy.

## Errors

### 2021-06-12

```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: No such file or directory
Is the server running locally and accepting
connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
```

## Sketches

### Database (ERD)

#### Movies/series

- You either add a movie or a series.
    - Information that is spesific to movie/series is stored in different tables.
    - Other than that, the rest is stored in the same tables.
    - 