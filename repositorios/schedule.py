from datetime import datetime
from modelos import Schedule 
from configs.pg_conn import get_db_connection

class ScheduleRepository:
    def create_schedule(schedule: Schedule):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Inserción de los datos del objeto User en la tabla
            insert_query = """
                INSERT INTO schedule (id_owner,id_day,start_hour,end_hour,available)
                VALUES (%s, %s, %s, %s, %s);
            """

            cursor.execute(insert_query, (schedule.id_owner,schedule.id_day,schedule.start_hour,schedule.end_hour,schedule.available))
            
            conn.commit()

        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()
            
    def get_schedule(input_id_owner: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("SELECT id_owner,id_day,start_hour,end_hour,available FROM schedule WHERE id_owner=%s"), (input_id_owner))

            # Obtiene todos los registros de la consulta
            records = cursor.fetchall()
            
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()

            # Convierte los registros a una lista de diccionarios y retorna la lista
            products = [{"id_day": id_day, "id_owner": id_owner, "start_hour": start_hour, "end_hour": end_hour, "available": available} for (id_owner,id_day,start_hour,end_hour,available) in records]
            
            return products
        
        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
            
    def delete_schedule(input_id_owner: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("DELETE FROM schedule WHERE id_owner=%s"), (input_id_owner))

            conn.commit()
            
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()

            return
        
        except Exception as e:
            print(f"Error al eliminar el horario: {e}")