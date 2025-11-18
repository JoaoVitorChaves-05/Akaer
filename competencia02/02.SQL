CREATE DATABASE IF NOT EXISTS exercicio02;
USE exercicio02;

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    amount INT,
    price DECIMAL(10,2),
    id_categories INT,
    FOREIGN KEY (id_categories) REFERENCES categories(id)
);

INSERT INTO categories (id, name) VALUES
(1, 'Superior'),
(2, 'Super Luxury'),
(3, 'Modern'),
(4, 'Nerd'),
(5, 'Infantile'),
(6, 'Robust'),
(9, 'Wood');

INSERT INTO products (id, name, amount, price, id_categories) VALUES
(1, 'Blue Chair',       30,  300.00,   9),
(2, 'Red Chair',        200, 2150.00,  2),
(3, 'Disney Wardrobe',  400, 829.50,   4),
(4, 'Blue Toaster',     20,   9.90,    3),
(5, 'Solar Panel',      30, 3000.25,   4);

-- Consulta SQL

SELECT p.name, c.name FROM products AS p
JOIN categories AS c ON p.id_categories = c.id
WHERE p.amount > 100 AND (
    p.id_categories = 1 OR
    p.id_categories = 2 OR
    p.id_categories = 3 OR
    p.id_categories = 6 OR
    p.id_categories = 9
)
ORDER BY c.id ASC;