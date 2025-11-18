CREATE DATABASE IF NOT EXISTS exercicio01;
USE exercicio01;

CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    street VARCHAR(255),
    city VARCHAR(255),
    state CHAR(2),
    credit_limit DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    orders_date DATE,
    id_customers INT,
    FOREIGN KEY (id_customers) REFERENCES customers(id)
);

INSERT INTO customers (id, name, street, city, state, credit_limit) VALUES
(1, 'Nicolas Diogo Cardoso',               'Acesso Um',                             'Porto Alegre',       'RS',  475),
(2, 'Cecilia Otília Rodrigues',            'Rua Sitaku Usuy',                       'Cianorte',           'PR', 3170),
(3, 'Augusto Fernando Carlos Eduardo Cardoso', 'Rua Baldomiro Koerich',           'Palhoça',            'SC', 1067),
(4, 'Nicolas Diogo Cardoso',               'Acesso Um',                             'Porto Alegre',       'RS',  475),
(5, 'Sabrina Melosia Gabriela Barros',     'Rua Engenheiro Tito Marques Fernandes', 'Porto Alegre',       'RS', 4312),
(6, 'Joaquin Diego Lorenzo Araújo',        'Rua Vitorino',                          'Novo Hamburgo',      'RS', 2314);

INSERT INTO orders (id, orders_date, id_customers) VALUES
(1, '2016-05-13', 3),
(2, '2016-02-12', 5),
(3, '2016-04-18', 2),
(4, '2016-09-07', 4),
(5, '2016-03-13', 6),
(6, '2016-08-05', 3);

-- Consulta SQL

SELECT c.name, o.id
FROM customers AS c
JOIN orders AS o ON c.id = o.id_customers
WHERE o.orders_date >= '2016-01-01' AND o.orders_date < '2016-07-01';