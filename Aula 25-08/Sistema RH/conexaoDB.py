import psycopg2


class ConexaoDB:
    def __init__(self, dbname, host, port, user, password):
        self.dbname = dbname
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = psycopg2.connect(
                dbname=self.dbname, host=self.host, port=self.port, user=self.user, password=self.password)

            self.cursor = self.conn.cursor()

            print("Conexão DB: Conexão Estabelecida com Sucesso!")

        except Exception as e:
            print("Conexão DB: Erro de conexão: ", e)
            self.desconectar()

    def desconectar(self):
        try:
            if self.cursor:
                self.cursor.close()
        except Exception as e:
            print("Conexão DB: Erro de desconexão: ", e)

        try:
            if self.conn:
                self.conn.close()
        except Exception as e:
            print("Conexão DB: Erro de desconexão: ", e)

        self.cursor = None
        self.conn = None

    def manipular(self, sql, variaveis):
        self.conectar()

        resultado = None

        try:
            self.cursor.execute(sql, variaveis)
            self.conn.commit()
            resultado = "DEU CERTO!"
        except Exception as e:
            print("Conexão DB: Erro de manipulação: ", e)
            self.conn.rollback()
            resultado = "DEU RUIM!"

        self.desconectar()
        return resultado

    def consultar(self, sql, variaveis):

        self.conectar()
        resultado = None

        try:

            self.cursor.execute(sql, variaveis)
            resultado = self.cursor.fetchall()

        except Exception as e:
            print("Conexão DB: Erro de consulta: ", e)
            resultado = None

        self.desconectar()
        return resultado
