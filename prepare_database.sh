#!/bin/bash
USER='coreuser'
PASSWORD='corpassword'
DB='core'

psql postgres << EOF
  CREATE USER ${USER} WITH ENCRYPTED PASSWORD '${PASSWORD}';

  ALTER ROLE ${USER} SET client_encoding TO 'utf8';
  ALTER ROLE ${USER} SET default_transaction_isolation TO 'read committed';

  CREATE DATABASE ${DB};
  GRANT ALL PRIVILEGES ON DATABASE core TO ${USER};

EOF
