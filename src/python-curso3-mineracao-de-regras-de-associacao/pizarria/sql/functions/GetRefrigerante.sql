DELIMITER $$
CREATE FUNCTION GetRefrigerante(valor_refrigerante FLOAT) returns VARCHAR(20)
BEGIN
	DECLARE refrigerante VARCHAR(20);
    IF(valor_refrigerante > 0) THEN
		SET refrigerante = 'Refrigerante Sim';
	ELSE
		SET refrigerante = 'Refrigerante Não';
	END IF;
    
    RETURN refrigerante;
END$$
DELIMITER ;