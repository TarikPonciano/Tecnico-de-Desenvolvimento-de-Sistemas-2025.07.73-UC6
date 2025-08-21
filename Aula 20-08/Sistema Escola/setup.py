import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

# Versão Aiven
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

try:
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                            password=DB_PASSWORD, port=DB_PORT, host=DB_HOST)

    cur = conn.cursor()

    cur.execute("SELECT VERSION();")

    resultado = cur.fetchall()

    print(resultado)

    cur.execute('''
CREATE TABLE IF NOT EXISTS aluno(
id_aluno integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_aluno varchar(255) NOT NULL,
cpf_aluno char(11) NOT NULL UNIQUE,
CONSTRAINT chk_cpf CHECK(LENGTH(cpf_aluno)=11)
                );
''')
    conn.commit()

    cur.close()
    conn.close()
except Exception as e:
    print("Erro:", e)
