CREATE USER searchly WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION
  PASSWORD 'searchly1234';


CREATE DATABASE searchly
    WITH
    OWNER = searchly
    ENCODING = 'utf8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default;


ALTER ROLE searchly IN DATABASE searchly SET search_path TO searchly;