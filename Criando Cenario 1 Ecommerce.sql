CREATE DATABASE "Empresa";

CREATE TABLE IF NOT EXISTS produto(
id_produto integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
categoria_id integer NOT NULL,
nome_produto varchar(255) NOT NULL,
preco_produto numeric(6,2) NOT NULL,
estoque_produto integer NOT NULL DEFAULT 0,
CONSTRAINT chk_preco CHECK(preco_produto > 0),
CONSTRAINT chk_estoque CHECK(estoque_produto >= 0)
);

CREATE TABLE IF NOT EXISTS cliente(
id_cliente integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_cliente varchar(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS categoria(
id_categoria integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_categoria varchar(255) NOT NULL UNIQUE
)

CREATE TABLE IF NOT EXISTS pedido(
id_pedido integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cliente_id integer NOT NULL,
data_pedido date NOT NULL DEFAULT '2025-01-01',
CONSTRAINT fk_pedido_cliente 
FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente)
ON UPDATE NO ACTION
ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS item(
id_item integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
pedido_id integer NOT NULL,
produto_id integer NOT NULL,
preco_item numeric(6,2) NOT NULL DEFAULT 0,
estoque_item integer NOT NULL DEFAULT 0,
CONSTRAINT chk_preco CHECK(preco_item > 0),
CONSTRAINT chk_estoque CHECK(estoque_item >= 0),
CONSTRAINT fk_item_pedido 
FOREIGN KEY (pedido_id) REFERENCES pedido(id_pedido) ON DELETE CASCADE,
CONSTRAINT fk_item_produto 
FOREIGN KEY (produto_id) REFERENCES produto(id_produto)
);

ALTER TABLE produto
ADD CONSTRAINT fk_produto_categoria FOREIGN KEY (categoria_id) REFERENCES categoria(id_categoria);
