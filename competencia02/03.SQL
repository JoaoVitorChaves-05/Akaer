CREATE DATABASE exercicio03;
USE exercicio03;

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    amount INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    id_categories INT NOT NULL,
    FOREIGN KEY (id_categories) REFERENCES categories(id)
);

INSERT INTO categories (id, name) VALUES
(1, 'wood'),
(2, 'luxury'),
(3, 'vintage'),
(4, 'modern'),
(5, 'super luxury');

INSERT INTO products (id, name, amount, price, id_categories) VALUES
(1, 'Two-doors wardrobe', 100, 800, 1),
(2, 'Dining table', 1000, 3000, 3),
(3, 'Towel holder', 10000, 25.50, 4),
(4, 'Computer desk', 350, 320.50, 2),
(5, 'Chair', 3000, 210.64, 4),
(6, 'Single bed', 750, 460, 1);

-- Consulta SQL

SELECT c.name, SUM(p.amount) AS sum
FROM categories AS c
JOIN products AS p ON p.id_categories = c.id
GROUP BY c.id, c.name
ORDER BY sum ASC;