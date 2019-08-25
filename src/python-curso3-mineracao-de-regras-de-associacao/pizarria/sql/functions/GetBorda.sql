DELIMITER $$
CREATE FUNCTION GetBorda(valor_borda FLOAT) returns VARCHAR(10)
BEGIN
	DECLARE borda VARCHAR(10);
    IF(valor_borda > 0) THEN
		SET borda = 'Borda Sim';
	ELSE
		SET borda = 'Borda Não';
	END IF;
    
    RETURN borda;
END$$
DELIMITER ;