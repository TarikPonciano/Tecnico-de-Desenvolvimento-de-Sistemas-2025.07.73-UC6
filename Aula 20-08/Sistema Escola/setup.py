import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

# Versão POSTGRESQL 17
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT") # Pode ser 5433

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
