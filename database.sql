CREATE TABLE users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_logged_in BOOLEAN DEFAULT FALSE,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE slider_elements (
    element_id INTEGER PRIMARY KEY NOT NULL,
    element_image_path VARCHAR(255) NOT NULL UNIQUE,
    element_place INTEGER(2) NOT NULL,
    element_title VARCHAR(255) NOT NULL,
    element_description VARCHAR(255) NOT NULL
);
