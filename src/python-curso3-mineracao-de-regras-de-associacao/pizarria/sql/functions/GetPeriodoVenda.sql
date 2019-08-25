DELIMITER $$
CREATE FUNCTION GetPeriodoVenda(hora_pedido TIME) returns VARCHAR(10)
BEGIN
	DECLARE periodo VARCHAR(10);
    
    IF(hora_pedido < '20:00:00') THEN
		SET periodo = 'Inicio';
	ELSEIF(hora_pedido >= '20:00:00' AND hora_pedido < '22:00:00') THEN
		SET periodo = 'Pico';
	ELSEIF(hora_pedido >= '22:00:00') THEN
		SET periodo = 'Final';
	END IF;
    
    RETURN periodo;
	
END$$
DELIMITER ;