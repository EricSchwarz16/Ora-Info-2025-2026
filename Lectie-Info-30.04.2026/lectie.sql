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

INSERT INTO customers (first_name, last_name, email) VALUES
('Eduard', 'Somfelean', 'edided@gmail.com');


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

SELECT first_name, email FROM customers
where first_name = 'Andrei';

SELECT * from orders
WHERE amout > 10 AND status = 'accepted'

SELECT SUM(amout) from orders -- Ssuma tuturor valorilor din tabel
SELECT AVG(amout) from orders -- Averageul valorilor de amount din tabel
SELECT COUNT(*) from orders -- numarul de entriuri din tabel

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