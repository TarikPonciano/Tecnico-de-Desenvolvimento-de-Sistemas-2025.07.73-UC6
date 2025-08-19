INSERT INTO categoria(nome_categoria)
VALUES ('Alimentos'), ('Eletrônicos'), ('Vestuário');

INSERT INTO produto(categoria_id, nome_produto, preco_produto, estoque_produto)
VALUES (1, 'Banana', 1.3, 20), (1, 'Biscoito Richester', 2.69, 50),
(2, 'Fone de Ouvido JBL', 299.99, 5), (2, 'Cabo USB Tipo-C', 25.99, 10),
(3, 'Cueca do Batman', 19.90, 1);

INSERT INTO cliente (nome_cliente)
VALUES ('Janaina'), ('Michael');

INSERT INTO pedido (cliente_id, data_pedido)
VALUES (1, CURRENT_DATE);

INSERT INTO item(pedido_id, produto_id, preco_item, estoque_item)
VALUES(1, 3, 1.3, 3), (1, 5, 299.99, 1);

SELECT * FROM item
WHERE pedido_id = 1;






