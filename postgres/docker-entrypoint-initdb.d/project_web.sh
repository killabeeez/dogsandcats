#!/bin/env bash

psql -U postgres -c "CREATE DATABASE $DB_NAME"
psql -U postgres -c "CREATE USER $DB_USER PASSWORD '$DB_PASS'"
psql -U postgres -c "ALTER ROLE $DB_USER SET client_encoding TO 'utf8'"
psql -U postgres -c "ALTER ROLE $DB_USER SET default_transaction_isolation TO 'read committed'"
psql -U postgres -c "ALTER ROLE $DB_USER SET timezone TO 'UTC'"
psql -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER"
