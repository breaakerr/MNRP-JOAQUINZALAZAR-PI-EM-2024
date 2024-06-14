import mysql.connector

# a diferencia del ejemplo, ya teniamos creadas los bloques de codigo con los comandos para ejecutar sobre la BD. Por lo que solo 
# establecemos una funcion para evitar el ingreso de datos al conectar con la base de datos.

def conectar_db():
    try:
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',  # 'localhost' o '127.0.0.1' si es local
            'database': 'proyecto'
        }

        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        return cnx, cursor

    except mysql.connector.Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        exit(1)