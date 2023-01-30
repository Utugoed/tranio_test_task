CREATE USER tranio;
ALTER USER tranio WITH password 'password';

CREATE DATABASE tranio;

ALTER DATABASE tranio OWNER TO tranio;
-- GRANT ALL PRIVILEGES ON DATABASE tranio TO tranio;

-- \c security tranio

-- GRANT ALL ON SCHEMA public TO tranio;
