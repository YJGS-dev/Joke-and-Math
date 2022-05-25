CREATE DATABASE joke;

CREATE TABLE IF NOT EXISTS joke
(
    id integer NOT NULL,
    joke text NOT NULL,
    CONSTRAINT "Joke_pkey" PRIMARY KEY (id)
)
