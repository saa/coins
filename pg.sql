CREATE USER coins WITH password 'coins';
CREATE DATABASE coins;
GRANT ALL ON DATABASE coins TO coins;
ALTER USER coins WITH createdb;