--- facem o comanda -> comenzi  -> ok
--- avem nevoie de detaliile comenzi -> DetaliiComenzi -> ok
--- actualizam stocul din depozit -> Stock depozit -> crapa

CREATE OR REPLACE PROCEDURE procesare_comanda()
LANGUAGE plpgsql
AS $$
DECLARE
    v_comanda_id INT;
BEGIN
  --BEGIN TRANSACTION
    INSERT INTO comenzi(client_id, status) 
    VALUES (1, 'procesare')
    RETURNING comanda_id INTO v_comanda_id;   -- <<< ; aici

    INSERT INTO DetaliiComenzi(comanda_id, produs_id, cantitate, pret_unitar)
    VALUES (v_comanda_id, 2, 1, 500);

    UPDATE StocDepozit
    SET cantitate_disponibila = cantitate_disponibila - 2
    WHERE produs_id = 2;

  -- COMMIT;
    RAISE NOTICE 'Succes';                    -- apostrof, nu ghilimele
EXCEPTION 
  -- ROLLBACK
    WHEN OTHERS THEN
        RAISE NOTICE 'Fail: %', SQLERRM;      -- îți arată și motivul
END;
$$;

call procesare_comanda();

BEGIN TRANSACTION


--Q1
--Q2
--Q3

COMMIT;

CREATE OR REPLACE FUNCTION log_modificare_stoc()
RETURNS TRIGGER AS
$$
BEGIN
  IF NEW.cantitate_disponibila < OLD.cantitate_disponibila THEN
    INSERT INTO IstoricModificari(tabel_afectat, actiune)
    VALUES ('StocDepozit', 'UPDATE');

    RAISE NOTICE 'stoc depozit updatat';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;


CREATE TRIGGER alerta_stoc
AFTER UPDATE ON StocDepozit
FOR EACH ROW
EXECUTE FUNCTION log_modificare_stoc()

select * from StocDepozit
WHERE produs_id = 2;

SELECT * FROM IstoricModificari;





















 