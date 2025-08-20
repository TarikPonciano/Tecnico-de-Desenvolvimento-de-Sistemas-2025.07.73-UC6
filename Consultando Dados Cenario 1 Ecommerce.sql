SELECT * FROM produto
WHERE estoque_produto < 10;

SELECT * FROM pedido
WHERE id_pedido = 1;

SELECT * FROM cliente
WHERE id_cliente = 1;

SELECT * FROM cliente, pedido
WHERE id_cliente = cliente_id;

SELECT id_cliente, nome_cliente, id_pedido, data_pedido
FROM cliente
INNER JOIN pedido ON id_cliente = cliente_id
WHERE id_pedido = 1;

SELECT SUM(preco_item * estoque_item) AS valor_total FROM item
WHERE pedido_id = 1;

INSERT INTO pedido
VALUES (default, 2, CURRENT_DATE);

INSERT INTO item
VALUES (default, 2, 7, 19.90,1), (default, 2, 6, 7.80,5);

SELECT nome_cliente, id_pedido, data_pedido, SUM(preco_item * estoque_item) as valor_total
FROM pedido
INNER JOIN cliente ON id_cliente = cliente_id
INNER JOIN item ON id_pedido = pedido_id
GROUP BY nome_cliente, id_pedido;
