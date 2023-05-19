from datetime import datetime
from modelos import User  
from configs.pg_conn import get_db_connection
import uuid

class UserRepository:
    def create_user(user: User):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
        
        cursor = conn.cursor()
                    
        insert_query = 'INSERT INTO users (id,full_name,password,email,created_at,updated_at,id_type,latitude,longitude,phone) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'

        try:
            cursor.execute(insert_query,(str(uuid.uuid4()), user.full_name, user.password, user.email,datetime.now(),datetime.now(), user.id_type,user.latitude,user.longitude,user.phone))
            conn.commit()
        except Exception as e:
            print(f"Error al insertar el valor: {e}")
            conn.rollback()
            
        #Cerrar la conexión
        cursor.close()
        conn.close() 
            
    def get_user(input_email: str,input_password: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("SELECT id,full_name,password,email,created_at,updated_at,id_type,latitude,longitude,phone FROM users WHERE email=%s AND password=%s"), (input_email,input_password))

            # Obtiene todos los registros de la consulta
            record = cursor.fetchone()
            
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()

            # Convierte los registros a una lista de diccionarios y retorna la lista
            user ={"id": record[0], "full_name": record[1], "password": record[2], "email": record[3], "created_at": record[4], "updated_at": record[5], "id_type": record[6], "latitude": record[7], "longitude": record[8], "phone": record[9]}
            
            return user
        
        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
    def update_user(user: User):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Actualización de los datos del objeto User en la tabla
            update_query = """
                UPDATE users SET updated_at=%s,latitude=%s,longitude=%s,phone=%s WHERE id=%s;
            """

            cursor.execute(update_query, (datetime.now(),user.latitude,user.longitude,user.phone, user.id))
            conn.commit()
            
            user ={"latitude":user.latitude,"longitude":user.longitude}

            return user
        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()
            
    def get_all_users():
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("SELECT us.id,us.full_name,us.password,us.email,us.created_at,us.updated_at,us.id_type,us.latitude,us.longitude,us.phone,CASE WHEN now()::time>=sch.start_hour AND now()::time<=sch.end_hour THEN true ELSE false END FROM users AS us JOIN schedule as sch ON us.id=sch.id_owner  WHERE sch.id_day=extract(ISODOW from now())"))

            # Obtiene todos los registros de la consulta
            records = cursor.fetchall()
            
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()

            # Creo la lista
            users = []
            
            # Convierte los registros a una lista de diccionarios y retorna la lista
            for record in records:
                user ={"id": record[0], "full_name": record[1], "password": record[2], "email": record[3], "created_at": record[4], "updated_at": record[5], "id_type": record[6], "latitude": record[7], "longitude": record[8], "phone": record[9], "status": record[10]}
                users.append(user)
                                   
            return users
        
        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")