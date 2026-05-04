-- Database: Lesson 4.05

-- DROP DATABASE IF EXISTS "Lesson 4.05";

CREATE DATABASE "Lesson 4.05"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'English_United States.1252'
    LC_CTYPE = 'English_United States.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

CREATE TABLE IF NOT EXISTS customers(
	id SERIAL PRIMARY KEY, -- unic pentru fiecare customer
	first_name VARCHAR(100) NOT NULL,
	last_name VARCHAR(100) NOT NULL,
	email VARCHAR(100) UNIQUE, -- unic pentru fiecare customer (nu putem avea mai multi customeri cu acelasi email)
	sign_up_date DATE DEFAULT CURRENT_DATE -- DEFAULT ne spune ce valoare va lua campul daca nu e specificat
);
CREATE TABLE IF NOT EXISTS orders(
	id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(id), -- FK catre customer
	order_date DATE DEFAULT CURRENT_DATE,
	amout NUMERIC(10, 2) NOT NULL, -- numar cu pana la 10 cifre si 2 zecimale
	status VARCHAR(100) DEFAULT 'pending'
);
ALTER TABLE customers ADD COLUMN IF NOT EXISTS phone_number VARCHAR(20);
ALTER TABLE orders ADD COLUMN IF NOT EXISTS product_name VARCHAR(20);
INSERT INTO customers (first_name, last_name, email) VALUES
('Eduard', 'Somfelean', 'edided@gmail.com'),
('Alex', 'Epic', 'alexepic@yahoo.com'),
('Robert', 'Ciocan', 'robertciocan@gmail.com');

SELECT * FROM customers;
INSERT INTO orders (customer_id, amout, status) VALUES
(1, 20, 'accepted'),
(1, 26, 'rejected'),
(2, 52, ''),
(2, 42, 'accepted'),
(3, 3, 'refunded');
SELECT * FROM orders;
UPDATE orders set status = 'accepted'
WHERE id = 3;
UPDATE orders set product_name = 'Microunde'
WHERE id = 1;
UPDATE orders set product_name = 'Föhn'
WHERE id = 2;
UPDATE orders set product_name = 'Pian'
WHERE id = 3;
UPDATE orders set product_name = 'Masa'
WHERE id = 4;
UPDATE orders set product_name = 'Computer'
WHERE id = 5;
SELECT first_name, email FROM customers
where first_name = 'Andrei';
SELECT * from orders
WHERE amout > 10 AND status = 'accepted';
SELECT SUM(amout) from orders; -- Ssuma tuturor valorilor din tabel
SELECT AVG(amout) from orders; -- Averageul valorilor de amount din tabel
SELECT COUNT(*) from orders; -- numarul de entriuri din tabel
SELECT status, SUM(amout) 
FROM orders
GROUP BY status
ORDER BY status
LIMIT 2; -- Suma primelor 2 comenzi dupa status ordonate alfabetic

--- inner join ---
--- vrem toti customeri care au comenzi si comenzile lor ---
SELECT *
FROM customers c
INNER JOIN orders o
on c.id = o.customer_id;
-- left join ---
SELECT *
FROM customers c
LEFT JOIN orders o
on c.id = o.customer_id;
-- right join --
SELECT *
FROM customers c
RIGHT JOIN orders o
on c.id = o.customer_id;
/*
1 Andrei
2 Mihai
3 Luca
4 Raul
...
...
..
...
100 Catalin
101 Vasile
*/
SELECT * FROM customers;
SELECT * FROM orders;

UPDATE customers SET phone_number = '0199288376'
WHERE id = 1;
UPDATE customers SET phone_number = '3459288376'
WHERE id = 2;
UPDATE customers SET phone_number = '0019288376'
WHERE id = 3;

-- Vrem sa vedem fiecare item cumparat de o persoana impreuna cu numele persoanei
SELECT c.first_name, c.last_name, o.product_name
FROM customers c JOIN orders o ON c.id = o.customer_id;

ALTER TABLE orders DROP COLUMN product_name; 
SELECT * FROM orders;

CREATE TABLE products(
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	order_id INT REFERENCES orders(id)
);

SELECT * FROM products

INSERT INTO products (name, order_id) VALUES
('Föhn', 1),
('Telefon', 2),
('Laptop', 1),
('T-Shirt', 2),
('Baterii', 3),
('Breloc', 5),
('Benzina', 4);

-- Vrem sa vedem fiecare item cumparat de o persoana impreuna cu numele persoanei
SELECT c.first_name, c.last_name, o.id, p.name
FROM customers c JOIN orders o ON c.id = o.customer_id
JOIN products p ON o.id = p.order_id

INSERT INTO orders (customer_id, amout, status) VALUES (2, '39', 'pending')

-- Gaseste orderurile fara produse sau produsele fara orderuri
SELECT o.id, p.order_id
FROM orders o LEFT JOIN products p ON o.id = p.order_id
WHERE p.order_id is NULL

SELECT o.id, p.name
FROM orders o FULL  JOIN products p ON o.id = p.order_id
WHERE o.id is NULL OR p.id is NULL

INSERT INTO products (name) VALUES ('Masina')
SELECT * from products
SELECT * from orders
SELECT * from customers

INSERT INTO products (name, order_id) VALUES ('Pat', 3)

-- O lista cu toti customerii + amount
SELECT c.first_name, c.last_name, COALESCE(avg(o.amout), 0)
FROM customers c left JOIN orders o ON c.id = o.customer_id
GROUP BY c.id;

INSERT INTO customers (first_name, last_name) VALUES ('Rob', 'Miguel')