delimiter $$
create function GetDiaSemana(data_pedido DATE) returns VARCHAR(10)
BEGIN
	return DAYNAME(data_pedido);
END$$
delimiter ;