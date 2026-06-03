DROP TRIGGER IF EXISTS trg_validare_detalii ON DetaliiComenzi;
DROP FUNCTION IF EXISTS fn_validare_detalii();

DROP TRIGGER IF EXISTS trg_log_status_comanda ON Comenzi;
DROP FUNCTION IF EXISTS fn_log_status_comanda();

DROP PROCEDURE IF EXISTS procesare_comanda_demo(INT, INT, INT, NUMERIC);

-- Trigger 1: Validare DetaliiComenzi
CREATE OR REPLACE FUNCTION fn_validare_detalii()
RETURNS TRIGGER AS
$$
DECLARE 
    v_stoc_curent INT;

BEGIN
    IF NEW.cantitate <= 0 THEN
        RAISE EXCEPTION 'Cantitatea trebuie sa fie > 0';

    END IF;

    SELECT cantitate_disponibila
    INTO v_stoc_curent
    FROM StocDepozit
    WHERE produs_id = NEW.produs_id
    FOR UPDATE;

    IF v_stoc_curent IS NULL THEN
        RAISE EXCEPTION 'Produsul % nu exista in StocDepozit', NEW.produs_id;
    
    END IF;

    IF v_stoc_curent < NEW.cantitate THEN
        RAISE EXCEPTION 'Stoc insuficient pentru produs % (stoc=%, cerut =%)',
            NEW.produs_id, v_stoc_curent, NEW.cantitate;
    
    END IF;

    RETURN NEW;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_validare_detalii
BEFORE INSERT OR UPDATE ON DetaliiComenzi
FOR EACH ROW
EXECUTE FUNCTION fn_validare_detalii();

--Trigger 2: Log Status Comanda
CREATE OR REPLACE FUNCTION fn_log_status_comanda()
RETURNS TRIGGER AS
$$
BEGIN
    IF OLD.status <> NEW.status THEN
        INSERT INTO IstoricModificari(tabel_afectat, actiune)
        VALUES ('Comenzi', 'UPDATE');
    
    END IF;

    RETURN NEW;

END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_log_status_comanda
AFTER UPDATE OF status ON Comenzi
FOR EACH ROW
EXECUTE FUNCTION fn_log_status_comanda();

-- Procedura: Procesare Comanda Demo
CREATE OR REPLACE PROCEDURE procesare_comanda_demo(
    p_client_id INT,
    p_produs_id INT,
    p_cantitate INT,
    p_pret_unitar NUMERIC 
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_comanda_id INT;

BEGIN
    INSERT INTO Comenzi(client_id, status)
    VALUES (p_client_id, 'procesare')
    RETURNING comanda_id INTO v_comanda_id;

    INSERT INTO DetaliiComenzi(comanda_id, produs_id, cantitate, pret_unitar)
    VALUES (v_comanda_id, p_produs_id, p_cantitate, p_pret_unitar);

    UPDATE StocDepozit
    SET cantitate_disponibila = cantitate_disponibila - p_cantitate
    WHERE produs_id = p_produs_id;

    UPDATE Comenzi
    SET status = 'confirmata'
    WHERE comanda_id = v_comanda_id;

    RAISE NOTICE = 'Comanda % procesata cu succes', v_comanda_id;

END;
$$;

-- Transaction 1: Procesare Comanda
BEGIN;
CALL procesare_comanda_demo(1, 2, 3, 100);
COMMIT;

--Transaction 2: Procesare Comanda cu Stoc Insuficient
BEGIN;
CALL procesare_comanda_demo(1, 2, 99999, 500);
ROLLBACK;

-- Rezultate

SELECT *
FROM StocDepozit
WHERE produs_id = 2;

SELECT *
FROM IstoricModificari
Order by 1 DESC;








    







