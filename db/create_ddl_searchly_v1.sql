CREATE SCHEMA searchly AUTHORIZATION searchly;

-- Sequences
CREATE SEQUENCE searchly_song_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

ALTER SEQUENCE searchly_song_id_seq
    OWNER TO searchly;

-- Tables
CREATE TABLE searchly_song
(
    id integer NOT NULL DEFAULT nextval('searchly_song_id_seq'::regclass),
    artist_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    song_name character varying(256) COLLATE pg_catalog."default" NOT NULL,
    lyrics character varying(4096) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT searchly_song_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE searchly_song
    OWNER to searchly;
