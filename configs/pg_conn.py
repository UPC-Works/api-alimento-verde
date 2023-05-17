import psycopg2


def get_db_connection():
    try:
        # Conexión a la base de datos
        conn = psycopg2.connect(
        host="localhost",
        port="5432",
        user="postgres",
        password="admin",
        database="alimento_verde"
        )
        print("Conexión exitosa")
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None


connection = get_db_connection()

if connection:
    print("Conexión exitosa")
    connection.close()
else:
    print("Error al conectar con la base de datos")