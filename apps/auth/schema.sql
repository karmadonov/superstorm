CREATE TABLE groups (
    id serial NOT NULL,
    name character varying(80) NOT NULL
)

CREATE TABLE users (
    id serial NOT NULL,
    email character varying(75) NOT NULL,
    password character varying(128) NOT NULL,
    gid integer references groups(id)
)
