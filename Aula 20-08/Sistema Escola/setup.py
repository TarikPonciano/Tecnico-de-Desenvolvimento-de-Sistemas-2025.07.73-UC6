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
DROP TABLE IF EXISTS matricula;
''')
    cur.execute('''
DROP TABLE IF EXISTS aluno;
''')
    cur.execute('''
DROP TABLE IF EXISTS disciplina;
''')
    cur.execute('''
CREATE TABLE IF NOT EXISTS aluno(
id_aluno integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_aluno varchar(255) NOT NULL,
cpf_aluno char(11) NOT NULL UNIQUE,
CONSTRAINT chk_cpf CHECK(LENGTH(cpf_aluno)=11)
                );
''')
# Caso queira resetar os dados da tabela também, usar o comando abaixo:

    cur.execute('''
CREATE TABLE IF NOT EXISTS disciplina(
id_disciplina integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
nome_disciplina varchar(255) NOT NULL,
ch_disciplina integer NOT NULL DEFAULT 0,
CONSTRAINT chk_ch CHECK (ch_disciplina >= 0)
                );
''')

    cur.execute('''
CREATE TABLE IF NOT EXISTS matricula(
id_matricula integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
aluno_id integer NOT NULL,
disciplina_id integer NOT NULL,
media_matricula NUMERIC (4,2) DEFAULT 0,
faltas_matricula integer DEFAULT 0,
CONSTRAINT fk_aluno_matricula FOREIGN KEY (aluno_id) REFERENCES aluno(id_aluno),
CONSTRAINT fk_disciplina_matricula FOREIGN KEY (disciplina_id) REFERENCES disciplina(id_disciplina),
CONSTRAINT chk_media CHECK (media_matricula >= 0 AND media_matricula <= 10)
);
''')

    # Criar 5 alunos, 2 disciplinas, 3 matriculas

    cur.execute('''
INSERT INTO aluno(nome_aluno, cpf_aluno)
VALUES ('Jefferson', '12345678910'), ('Zeca', '12345678911'), ('Manel','12345678912'), ('Maicao', '12345678913'), ('Ana', '12345678914') ON CONFLICT DO NOTHING;
''')

    conn.commit()

    cur.close()
    conn.close()
except Exception as e:
    print("Erro:", e)
