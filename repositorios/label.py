from datetime import datetime
from modelos import Label 
from configs.pg_conn import get_db_connection
import uuid

class LabelRepository:
    def create_label(label: Label):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Inserción de los datos del objeto User en la tabla
            insert_query = """
                INSERT INTO label (id,id_owner,name)
                VALUES (%s, %s, %s);
            """

            cursor.execute(insert_query, (str(uuid.uuid4()), label.id_owner, label.name))
            
            conn.commit()

        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()
            
    def get_label(input_id_owner: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("SELECT id,id_owner,name FROM stock_offer WHERE id_owner=%s"), (input_id_owner))

            # Obtiene todos los registros de la consulta
            records = cursor.fetchall()
            
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()

            # Convierte los registros a una lista de diccionarios y retorna la lista
            labels = [{"id": id, "id_owner": id_owner, "name": name} for (id,id_owner,name) in records]
            
            return labels
        
        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
            
    def update_label(label: Label):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Actualización de los datos del objeto User en la tabla
            update_query = """
                UPDATE label SET name=%s WHERE id=%s;
            """

            cursor.execute(update_query, (label.name, label.id))
            
            conn.commit()

        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()