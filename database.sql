CREATE TABLE users (
    user_id INTEGER PRIMARY KEY NOT NULL,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    is_logged_in BOOLEAN DEFAULT FALSE,
    is_admin BOOLEAN DEFAULT FALSE
);

CREATE TABLE slider_images (
    element_id INTEGER PRIMARY KEY NOT NULL,
    element_image_path VARCHAR(255) NOT NULL UNIQUE,
    element_title VARCHAR(255) NOT NULL,
    element_description VARCHAR(255),
    element_slider VARCHAR(255) NOT NULL
);

CREATE TABLE service_cards (
    service_id INTEGER PRIMARY KEY NOT NULL,
    service_image_path VARCHAR(255) UNIQUE NOT NULL,
    service_title VARCHAR(255) UNIQUE NOT NULL,
    service_description VARCHAR(255) NOT NULL,
    service_link VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY NOT NULL,
    customer_image_path VARCHAR(255) UNIQUE NOT NULL,
    customer_name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE information 
(
    email VARCHAR(255) PRIMARY KEY NOT NULL,
    main_phone VARCHAR(255) NOT NULL,
    other_phone VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    city VARCHAR(255) NOT NULL,
    footer_description VARCHAR(255) NOT NULL
);
