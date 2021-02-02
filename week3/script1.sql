CREATE DATABASE "MOVIE_DB";

\c MOVIE_DB

CREATE TABLE "MOVIE" (
  "id" int,
  "title" text,
  "year" date,
  "produced_by" int,
  "genre" int,
  "director" int,
  "actors" int,
  "plot" text,
  "quotes" int,
  PRIMARY KEY ("id", "title", "year")
);

CREATE TABLE "PRODUCTION_COMPANY" (
  "id" int PRIMARY KEY,
  "name" text,
  "address" text
);

CREATE TABLE "GENRE" (
  "id" int PRIMARY KEY,
  "name" text
);

CREATE TABLE "QUOTE" (
  "id" int,
  "quote" text
);

CREATE TABLE "PERSON" (
  "id" int PRIMARY KEY,
  "name" text,
  "occupation" int
);

CREATE TABLE "OCCUPATION" (
  "id" int PRIMARY KEY,
  "title" text
);

CREATE TABLE "actor_movie_role" (
  "actor" int,
  "movie" int,
  "role" text
);

ALTER TABLE "actor_movie_role" ADD FOREIGN KEY ("actor") REFERENCES "PERSON" ("id");

ALTER TABLE "actor_movie_role" ADD FOREIGN KEY ("movie") REFERENCES "MOVIE" ("id");

ALTER TABLE "PERSON" ADD FOREIGN KEY ("occupation") REFERENCES "OCCUPATION" ("id");

ALTER TABLE "MOVIE" ADD FOREIGN KEY ("produced_by") REFERENCES "PRODUCTION_COMPANY" ("id");

ALTER TABLE "MOVIE" ADD FOREIGN KEY ("genre") REFERENCES "GENRE" ("id");

ALTER TABLE "MOVIE" ADD FOREIGN KEY ("director") REFERENCES "PERSON" ("id");

ALTER TABLE "MOVIE" ADD FOREIGN KEY ("actors") REFERENCES "PERSON" ("id");

ALTER TABLE "MOVIE" ADD FOREIGN KEY ("quotes") REFERENCES "QUOTE" ("id");

