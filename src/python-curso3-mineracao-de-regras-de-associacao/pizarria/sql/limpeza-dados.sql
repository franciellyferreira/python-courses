SELECT * FROM pedidos;

ALTER TABLE pedidos DROP COLUMN numero;
ALTER TABLE pedidos DROP COLUMN cliente;
ALTER TABLE pedidos DROP COLUMN endereco;
ALTER TABLE pedidos DROP COLUMN telefone;
ALTER TABLE pedidos DROP COLUMN valor_pizza;
ALTER TABLE pedidos DROP COLUMN valor_entrega;
ALTER TABLE pedidos DROP COLUMN hora_entrega;

SELECT * FROM pedidos;
SELECT MAX(data_pedido), MIN(data_pedido) FROM pedidos; -- busca maior e menor data
DELETE FROM pedidos WHERE year(data_pedido) >= 2015; -- remove pedidos teste de 2015
SELECT DAYNAME(data_pedido) FROM pedidos; -- melhor dia da semana pra vendas
SELECT @@lc_time_names;
SET lc_time_names = 'pt_BR';

SELECT * FROM pedidos;
SELECT MAX(hora_pedido), MIN(hora_pedido) FROM pedidos; -- busca maior e menor data
