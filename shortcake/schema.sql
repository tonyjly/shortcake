CREATE TABLE links (
    id              INTEGER NOT NULL PRIMARY KEY,
    long_link       TEXT NOT NULL,
    short_link_id   TEXT NOT NULL REFERENCES short_links (id)
)

CREATE TABLE short_links (
    id              INTEGER NOT NULL PRIMARY KEY,
    url             TEXT NOT NULL,
    date_created    DATE NOT NULL,
    times_accessed  INTEGER
)
