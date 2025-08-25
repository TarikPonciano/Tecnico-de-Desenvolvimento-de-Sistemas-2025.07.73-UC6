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
VALUES ('Tolkien'), ('Dan Brown'), ('Clarice Lispector'), ('Machado de Assis'), ('Conceição Evaristo'), ('Jackson Rodrigues'), ('Kishimoto'), ('Akira Toriyama') ON CONFLICT DO NOTHING;
''')

    cur.execute('''
    INSERT INTO membro(nome_membro, email_membro)
    VALUES ('Manoel', 'manoel@gmail.com'), ('Joaquim','joaquim@gmail.com'), ('Rafaela', 'rafaela@gmail.com'), ('Maria Silva', 'mariasilva@gmail.com') ON CONFLICT DO NOTHING;
                ''')

    cur.execute('''
    INSERT INTO livro(titulo_livro, ano_livro, autor_id)
    VALUES('Código Da Vinci', 2005, 2), ('Senhor dos Anéis', 1942, 1), ('Anjos e Demonios', 2007, 2), ('Naruto', 2001, 7), ('Dragon Ball', 1980, 8), ('Dr Slump', 1977, 8) ON CONFLICT DO NOTHING;
''')

    cur.execute('''
    INSERT INTO emprestimo (livro_id, membro_id) (
    VALUES (1,2), (2,3), (5,1), (3,2), (6,4)
                ) ON CONFLICT DO NOTHING;
''')
    conn.commit()

    cur.execute('''
    UPDATE membro
    SET
    email_membro = 'manoelgomes@gmail.com'
    WHERE
    id_membro = 1;
''')

    cur.execute('''
    UPDATE emprestimo
    SET devolucao_emprestimo = CURRENT_DATE
    WHERE id_emprestimo = 1;
''')

    cur.execute('''
    DELETE FROM livro
    WHERE titulo_livro = 'Naruto';
''')
    conn.commit()
# Método Manual - Consultas Múltiplas
#     cur.execute('''
# SELECT * FROM emprestimo
# WHERE devolucao_emprestimo is null
# ORDER BY id_emprestimo ASC;
# ''')

#     resultado = cur.fetchall()
#     livrosEmprestados = []

#     for r in resultado:
#         livrosEmprestados.append(r[2])

#     cur.execute('''
# SELECT * FROM livro
# WHERE id_livro IN %s;
# ''', (tuple(livrosEmprestados),))

#     resultado = cur.fetchall()
#     print(resultado)

# Exibir livros emprestados porém não devolvidos
    cur.execute('''
SELECT id_livro, titulo_livro, ano_livro, data_emprestimo  FROM emprestimo
RIGHT JOIN livro ON livro_id = id_livro
WHERE devolucao_emprestimo is not null
ORDER BY id_emprestimo ASC;
''')
    resultado = cur.fetchall()
    print(resultado)

    cur.execute('''
SELECT nome_membro, titulo_livro, nome_autor, data_emprestimo, devolucao_emprestimo FROM emprestimo
INNER JOIN membro ON membro_id = id_membro
INNER JOIN livro ON livro_id = id_livro                
INNER JOIN autor ON autor_id = id_autor
WHERE nome_membro LIKE 'Maria%';
''')
    resultado = cur.fetchall()
    print(resultado)

    cur.execute('''
    SELECT COUNT(id_livro) FROM livro
    WHERE ano_livro > 2000; ''')

    resultado = cur.fetchall()

    print(f'Livros publicados após 2000: {resultado[0][0]}')

    cur.execute('''
    ALTER TABLE membro
    ADD COLUMN telefone_membro VARCHAR(11);''')

#     cur.execute('''
#     UPDATE membro
#     SET telefone_membro = 'SEM TEL'
#     WHERE telefone_membro is null;
# ''')

#     cur.execute('''
#     ALTER TABLE membro
#     ALTER COLUMN telefone_membro SET NOT NULL;
# ''')

    cur.executemany('''
    ALTER TABLE emprestimo
    DROP COLUMN id_emprestimo;
            
    ALTER TABLE emprestimo
    ADD PRIMARY KEY(membro_id, livro_id);
''', [])

    cur.execute('''
    ALTER TABLE livro
    ADD CONSTRAINT chk_ano_publicacao CHECK (ano_livro > 1900);
''')

    conn.commit()

    cur.close()
    conn.close()

except Exception as e:
    print("Erro:", e)
