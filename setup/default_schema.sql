BEGIN;

    CREATE OR REPLACE FUNCTION set_creation_date() RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $BODY$BEGIN
       new.creation_date = now();
       RETURN new;
    END;$BODY$;

    CREATE OR REPLACE FUNCTION update_modification_date() RETURNS TRIGGER
    LANGUAGE plpgsql AS
    $BODY$BEGIN
       new.modification_date = now();
       RETURN new;
    END;$BODY$;

    CREATE TABLE items (
        id SERIAL PRIMARY KEY NOT NULL,
        name TEXT,
        description TEXT,
        quantity INTEGER,
        image TEXT,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now()
    );

    CREATE TRIGGER items_creation_date
        BEFORE INSERT ON items
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER items_modification_date2
        BEFORE INSERT OR UPDATE ON items
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON items TO readwrite;
    GRANT SELECT, UPDATE ON items_id_seq TO readwrite;


    CREATE TABLE tags (
        id SERIAL PRIMARY KEY NOT NULL,
        name TEXT,
        description TEXT,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now()
    );

    CREATE TRIGGER tags_creation_date
        BEFORE INSERT ON tags
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER tags_modification_date
        BEFORE INSERT OR UPDATE ON tags
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON tags TO readwrite;
    GRANT SELECT, UPDATE ON tags_id_seq TO readwrite;


    CREATE TABLE tags_to_items (
        item_id INTEGER NOT NULL,
        tag_id INTEGER NOT NULL,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now(),
        PRIMARY KEY(item_id, tag_id)
    );

    ALTER TABLE tags_to_items ADD FOREIGN KEY (item_id)
        REFERENCES items(id) ON DELETE CASCADE;
    ALTER TABLE tags_to_items ADD FOREIGN KEY (tag_id)
        REFERENCES tags(id) ON DELETE CASCADE;

    CREATE TRIGGER tags_to_items_creation_date
        BEFORE INSERT ON tags_to_items
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER tags_to_items_modification_date
        BEFORE INSERT OR UPDATE ON tags_to_items
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON tags_to_items TO readwrite;


    CREATE TABLE users (
        id SERIAL PRIMARY KEY NOT NULL,
        username TEXT,
        password TEXT,
        locked BOOLEAN DEFAULT false,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now()
    );

    CREATE TRIGGER users_creation_date
        BEFORE INSERT ON users
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER users_modification_date
        BEFORE INSERT OR UPDATE ON users
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON users TO readwrite;
    GRANT SELECT, UPDATE ON users_id_seq TO readwrite;

    CREATE TABLE permissions (
        id SERIAL PRIMARY KEY NOT NULL,
        name TEXT,
        description TEXT,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now()
    );

    CREATE TRIGGER permissions_creation_date
        BEFORE INSERT ON permissions
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER permissions_modification_date
        BEFORE INSERT OR UPDATE ON permissions
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON permissions TO readwrite;
    GRANT SELECT, UPDATE ON permissions_id_seq TO readwrite;


    CREATE TABLE permissions_to_users (
        permission_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        creation_date TIMESTAMP DEFAULT now(),
        modification_date TIMESTAMP DEFAULT now(),
        PRIMARY KEY(permission_id, user_id)
    );

    ALTER TABLE permissions_to_users ADD FOREIGN KEY (permission_id)
        REFERENCES permissions(id) ON DELETE CASCADE;
    ALTER TABLE permissions_to_users ADD FOREIGN KEY (user_id)
        REFERENCES users(id) ON DELETE CASCADE;

    CREATE TRIGGER permissions_to_users_creation_date
        BEFORE INSERT ON permissions_to_users
        FOR EACH ROW EXECUTE PROCEDURE set_creation_date();
    CREATE TRIGGER permissions_to_users_modification_date
        BEFORE INSERT OR UPDATE ON permissions_to_users
        FOR EACH ROW EXECUTE PROCEDURE update_modification_date();

    GRANT SELECT, INSERT, UPDATE, DELETE ON permissions_to_users TO readwrite;

COMMIT;
