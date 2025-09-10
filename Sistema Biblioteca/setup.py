import psycopg2
import dotenv
import os
from Control.ConexaoDB import ConexaoDB

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

meuBanco = ConexaoDB(dbname=DB_NAME, host=DB_HOST,
                     port=DB_PORT, user=DB_USER, password=DB_PASSWORD)


meuBanco.manipular("DROP TABLE IF EXISTS aluguel;")
meuBanco.manipular("DROP TABLE IF EXISTS emprestimo;")
meuBanco.manipular("DROP TABLE IF EXISTS livro;")
meuBanco.manipular("DROP TABLE IF EXISTS cliente;")

meuBanco.manipular('''CREATE TABLE IF NOT EXISTS cliente(
                   id_cliente integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                   nome_cliente varchar(255) NOT NULL);''')

meuBanco.manipular('''CREATE TABLE IF NOT EXISTS livro(
                   id_livro integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                   titulo_livro varchar(255) NOT NULL);''')

meuBanco.manipular('''
CREATE TABLE IF NOT EXISTS aluguel(
id_aluguel integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
cliente_id integer NOT NULL,
livro_id integer NOT NULL,
CONSTRAINT fk_cliente_aluguel FOREIGN KEY (cliente_id) REFERENCES cliente(id_cliente),
CONSTRAINT fk_livro_aluguel FOREIGN KEY (livro_id) REFERENCES livro(id_livro)
);
''')
