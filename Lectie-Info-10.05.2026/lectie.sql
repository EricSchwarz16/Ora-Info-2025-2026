CREATE TABLE customers ON DELETE CASCADE(
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
);
 
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
SELECT c.first_name, c.last_name, COALESCE(sum(o.amout), 0)
FROM customers c left JOIN orders o ON c.id = o.customer_id
GROUP BY c.id;
 
CREATE OR REPLACE VIEW customer_spending AS
SELECT c.first_name, c.last_name, COALESCE(sum(o.amout), 0)
FROM customers c left JOIN orders o ON c.id = o.customer_id
GROUP BY c.id;
 
SELECT * FROM (
	SELECT c.first_name, c.last_name, COALESCE(sum(o.amout), 0)
	FROM customers c left JOIN orders o ON c.id = o.customer_id
	GROUP BY c.id
) AS cs
INNER JOIN customers c 
ON c.first_name = cs.first_name;
 
--- frumos
SELECT * FROM customer_spending cs
INNER JOIN customers c 
ON c.first_name = cs.first_name;
 
 
 
 
INSERT INTO customers (first_name, last_name) VALUES ('Rob', 'Miguel')
 
 
SELECT * FROM customers;
SELECT * from orders;
 
 
SELECT c.id, c.last_name, c.email, COALESCE(SUM(o.amout), 0) 
FROM customers c 
INNER JOIN orders o
ON c.id = o.customer_id
GROUP BY c.id
ORDER BY c.id;
 
SELECT c.id, c.last_name, c.email, aux.total_expense
FROM customers c
INNER JOIN (
	SELECT customer_id, SUM(amout) AS total_expense
	FROM orders
	GROUP BY customer_id
) AS aux
ON aux.customer_id = c.id
ORDER BY c.id;
 
SELECT * FROM customer_spending;
 
 
 
 
 
 
 
 
 
 
 
SELECT * FROM customers
SELECT * FROM orders
 
-- FK -> Contraint sa arate spre alt tabel
-- PK -> constraint -> sa fie unioc
-- UNIQUE
-- NOT NULL
 
 
 
ALTER TABLE orders
ADD CONSTRAINT IF NOT EXISTS chk_amount_positive CHECK(amout >= 0);
 
INSERT INTO orders (customer_id, amout, status) VALUES (1, -1232134, 'pending');
 
DELETE FROM orders where amout < 0;
 
 
ALTER TABLE customers
ADD CONSTRAINT unique_phone UNIQUE(phone_number)
 
SELECT * FROM customers
SELECT * FROM orders
 
DELETE FROM customers WHERE id = 1
 
ALTER TABLE orders DROP CONSTRAINT orders_customer_id_fkey;
 
ALTER TABLE orders
ADD CONSTRAINT orders_delete_casscade_fk
FOREIGN KEY (customer_id) REFERENCES customers(id) ON DELETE CASCADE;
 
 
--- 
 
 
--- AVG, SUM, MIN, MAX, COUNT
--- FUNCTII -> RETURNEAZA -> INT/LONG LONG/ CHAR
--- PROCEDURI -> NU RETURNEAZA -> VOID
 
CREATE OR REPLACE FUNCTION calculeaza_tva(valoare NUMERIC)
RETURNS NUMERIC AS $$
BEGIN
	RETURN valoare + (valoare * 0.19);
END;
$$ LANGUAGE plpgsql;
 
SELECT calculeaza_tva(amout) as pret_cu_tva 
FROM orders
 
CREATE OR REPLACE PROCEDURE creaza_tabel()
AS $$
BEGIN
	CREATE TABLE products(
	id SERIAL PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	order_id INT REFERENCES orders(id)
);
END;
$$ LANGUAGE plpgsql;
 
CALL creaza_tabel()
 
-- aici plasam o comanda pentru un produs care nu este in baza de date!!!!!!!!
CREATE OR REPLACE PROCEDURE plaseaza_comanda(
	p_customer_id INT,
	p_suma NUMERIC,
	p_nume_produs VARCHAR(100)
)
AS $$
DECLARE
	new_order_id INT;
BEGIN
	--- cream un order si sa-l salvam
	INSERT INTO orders(customer_id, amout, status)
	VALUES (p_customer_id, p_suma, 'pending') --pot sa returnez intr-o variabala un element din linia noua creata
	RETURNING id INTO new_order_id;
 
	-- adaug produs, si sa il legam de order-ul creat
	INSERT INTO products (name, order_id)
	VALUES (p_nume_produs, new_order_id);
END;
$$ LANGUAGE plpgsql;
 
CALL plaseaza_comanda(2, 500, 'Fion');
 
 
 
SELECT * FROM customers
SELECT * FROM orders
select * from products
 