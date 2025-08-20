import psycopg2
import dotenv

# Versão POSTGRESQL 17
DB_NAME = "Escola2"
DB_USER = "postgres"
DB_PASSWORD = "senac"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"  # Pode ser 5433

# Versão Aiven
DB_NAME = "Escola2"
DB_USER = "****************"
DB_PASSWORD = "************"
DB_HOST = "*************"
DB_PORT = "************"

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        host=DB_HOST, port=DB_PORT, password=DB_PASSWORD)

cur = conn.cursor()

cur.execute("SELECT VERSION()")

resultado = cur.fetchall()

print(resultado)

cur.close()
conn.close()
