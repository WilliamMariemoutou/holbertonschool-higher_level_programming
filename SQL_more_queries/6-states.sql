-- Creates a new database and table

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states(
    id INT IS NOT NULL UNIQUE PRIMARY KEY,
    name VARHAR(256)
);
