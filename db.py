import oracledb

# faz a conexão com o banco sql e cria os cursores para as operações do crud
def conectar():
    try:
        connection = oracledb.connect(
            user="rm563717",
            password="310307",
            dsn="oracle.fiap.com.br:1521/ORCL"
        )

        cursor = connection.cursor()
    except Exception as e:
        print("Erro na conexão: ", e)
        return None, None
    else:
        return connection, cursor

# recebe o código sql e o tipo de cursor para fazer a operação equivalente no banco
def executar_comando(sql, params=None, fetch=True):
    connection, cursor = conectar()
    if not connection:
        return None

    try:
        cursor.execute(sql, params or {})
        resultado = None
        if fetch:
            resultado = cursor.fetchall()
        connection.commit()
    except Exception as e:
        print("Erro ao executar comando: ", e)
        resultado = None
    finally:
        cursor.close()
        connection.close()
    
    return resultado