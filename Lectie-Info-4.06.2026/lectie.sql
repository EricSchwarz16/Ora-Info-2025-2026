
SELECT * FROM Produse

-- adaugam o coloana cu un array de taguri

ALTER TABLE Produse ADD COLUMN taguri TEXT[]; 
--tipul de date este text si prin [] -> specificam ca avem un array de text


SELECT * FROM Produse

--- prin array specificam ca creeam un array si tipul de date este luat implicit deoarece folosim ''
UPDATE Produse SET taguri = ARRAY['basic', '4GB Ram', 'XIAOMI'] 
WHERE produs_id % 2 = 1;

--- vrem toate produsele premium
--- AVG, SUM -> operau pe mai multe coloane deodata
SELECT * FROM Produse 
WHERE 'premium' = ANY(taguri)


ALTER TABLE Produse ADD COLUMN specificatii JSONB;

UPDATE Produse SET specificatii = '{"test":"8GB", "tip":"premium", "culoare":"negru", "descriere" : {
  "user":"Bogdan",
  "data":"24.11.2025",
  "content":"Produsul este foarte bun",
  "note de la oameni": [1,2,3,4,5,10,10,10]
}}'
WHERE produs_id % 2 = 1;

SELECT * FROM Produse
WHERE specificatii->>'culoare' = 'rosu'


SELECT * FROM Produse
WHERE specificatii ? 'test' --ma uit doar unde am in specificatii cheia ram


SELECT * FROM Produse
WHERE nume ~ '[^0-9][0-9]{2}([^0-9]|$)'

-- [^a-z]
-- ([a-z]|b)
-- ([^0-9]|$)

--- Scaun  Ergonomic -> cautare

--- FTS

SELECT * FROM Produse
WHERE nume LIKE 'Birou%'



SELECT nume, pret FROM Produse
WHERE
to_tsvector('simple', nume) @@ to_tsquery('simple', 'scaun & ergonomic');

 