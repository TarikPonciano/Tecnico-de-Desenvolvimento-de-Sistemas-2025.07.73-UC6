import psycopg2
import dotenv
import os
import datetime

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


try:
    conn = psycopg2.connect(dbname=DB_NAME, host=DB_HOST,
                            port=DB_PORT, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    cur.executemany('''
DROP TABLE IF EXISTS funcionario;
DROP TABLE IF EXISTS departamento; 
''', [])

    # SQL
    cur.execute('''CREATE TABLE IF NOT EXISTS departamento(
                id_departamento integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
                nome_departamento varchar(255) NOT NULL);''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS funcionario(
    id_funcionario integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_funcionario varchar(255) NOT NULL,
    cpf_funcionario char(11) NOT NULL,
    salario_funcionario NUMERIC(10,2) NOT NULL DEFAULT 1512.00,
    cargo_funcionario varchar(255) NOT NULL DEFAULT 'Funcionario',
    departamento_id integer,
    CONSTRAINT chk_cpf_tamanho CHECK (LENGTH(cpf_funcionario) = 11),
    CONSTRAINT chk_salario_valido CHECK (salario_funcionario >= 1512.00),
    CONSTRAINT fk_funcionario_departamento FOREIGN KEY (departamento_id) REFERENCES departamento(id_departamento) ON DELETE SET NULL
                );
''')

    conn.commit()
    cur.close()
    conn.close()
except Exception as e:
    print("ERRO:", e)
