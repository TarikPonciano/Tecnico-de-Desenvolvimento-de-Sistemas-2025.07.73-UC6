import dotenv
import os
from conexaoDB import ConexaoDB

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

meuBanco = ConexaoDB(dbname=DB_NAME, host=DB_HOST,
                     port=DB_PORT, user=DB_USER, password=DB_PASSWORD)

meuBanco.manipular('''DROP TABLE IF EXISTS item;''')
meuBanco.manipular('''DROP TABLE IF EXISTS venda;''')
meuBanco.manipular('''DROP TABLE IF EXISTS produto;''')
meuBanco.manipular('''DROP TABLE IF EXISTS cliente;''')

meuBanco.manipular('''
CREATE TABLE IF NOT EXISTS cliente(
id_cliente integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_cliente varchar(255) NOT NULL );
''')

meuBanco.manipular('''
CREATE TABLE IF NOT EXISTS produto(
id_produto integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_produto varchar(255) NOT NULL,
preco_produto NUMERIC(6,2) NOT NULL DEFAULT 0.00,
estoque_produto integer NOT NULL DEFAULT 0,
CONSTRAINT chk_preco CHECK (preco_produto >= 0),
CONSTRAINT chk_estoque CHECK (estoque_produto >= 0)
);
''')

meuBanco.manipular('''
CREATE TABLE IF NOT EXISTS venda(
id_venda integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cliente_id integer NOT NULL,
total_venda NUMERIC(10,2) NOT NULL DEFAULT 0.00,
data_venda TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT chk_total CHECK (total_venda >= 0),
CONSTRAINT fk_cliente_venda FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente))
''')

meuBanco.manipular('''
CREATE TABLE IF NOT EXISTS item(
id_item integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
venda_id integer NOT NULL,
produto_id integer NOT NULL,
quantidade_item integer NOT NULL default 1,
preco_item NUMERIC(6,2) NOT NULL default 0.00,
CONSTRAINT chk_qtd CHECK (quantidade_item >= 1),
CONSTRAINT chk_preco CHECK (preco_item >= 0),
CONSTRAINT fk_venda_item FOREIGN KEY (venda_id) REFERENCES venda(id_venda) ON DELETE CASCADE,
CONSTRAINT fk_produto_item FOREIGN KEY (produto_id) REFERENCES produto(id_produto) 
                   );
''')
