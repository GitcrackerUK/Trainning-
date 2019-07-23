CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    isbn  integer  not null ,
    title integer  NOT NULL,
    author VARCHAR NOT NULL,
    year varchar  NOT NULL
);

CREATE TABLE passangers (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);