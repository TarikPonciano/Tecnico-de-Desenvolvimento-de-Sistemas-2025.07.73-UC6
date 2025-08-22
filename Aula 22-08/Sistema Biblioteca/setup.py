import psycopg2
import dotenv
import os

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

    cur.execute('''
DROP TABLE IF EXISTS emprestimo;
''')
    cur.execute('''
DROP TABLE IF EXISTS livro;
''')
    cur.execute('''
DROP TABLE IF EXISTS membro;
''')
    cur.execute('''
DROP TABLE IF EXISTS autor;
''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS autor(
    id_autor integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_autor varchar(255) NOT NULL
);
''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS membro(
    id_membro integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    nome_membro varchar(255) NOT NULL,
    email_membro varchar(255) NOT NULL,
    CONSTRAINT chk_email CHECK (email_membro ILIKE '%@%')
);
''')
    
    cur.execute('''
    CREATE TABLE IF NOT EXISTS livro(
    id_livro integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    autor_id integer NOT NULL,
    titulo_livro varchar(255) NOT NULL,
    ano_livro integer NOT NULL,
    CONSTRAINT fk_autor_livro FOREIGN KEY (autor_id) REFERENCES autor(id_autor)
                );
                ''')
    
    cur.execute('''
    CREATE TABLE IF NOT EXISTS emprestimo(
    id_emprestimo integer GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    membro_id integer NOT NULL,
    livro_id integer NOT NULL,
    data_emprestimo date NOT NULL DEFAULT CURRENT_DATE,
    devolucao_emprestimo date DEFAULT NULL,
    CONSTRAINT fk_membro_emprestimo FOREIGN KEY (membro_id) REFERENCES membro(id_membro),
    CONSTRAINT fk_livro_emprestimo FOREIGN KEY (livro_id) REFERENCES livro(id_livro)
                );
''')
    
    conn.commit()

    cur.execute('''
INSERT INTO autor(nome_autor)
VALUES ('Tolkien'), ('Dan Brown'), ('Clarice Portela'), ('Machado de Assis'), ('Conceição Evaristo'), ('Jackson Rodrigues') ON CONFLICT DO NOTHING;
''')
    conn.commit()


    cur.close()
    conn.close()

except Exception as e:
    print("Erro:", e)
