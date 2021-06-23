BEGIN;
    
    INSERT INTO permissions (name, description) VALUES
        ('Admin', 'Controls permissions'),
        ('Editor', 'Can add/remove/update items');

    INSERT INTO users (username, password) VALUES
        ('admin', 'not_really_a_password_yet'),
        ('editor', 'not_really_a_password_yet'),
        ('viwer', 'not_really_a_password_yet');

    INSERT INTO permissions_to_users (permission_id, user_id) VALUES
        (
            (SELECT id FROM permissions WHERE name = 'Admin'),
            (SELECT id FROM users WHERE username = 'admin')
        ),
        (
            (SELECT id FROM permissions WHERE name = 'Editor'),
            (SELECT id FROM users WHERE username = 'editor')
        );

COMMIT;