from datetime import datetime
from modelos import Product 
from configs.pg_conn import get_db_connection
import json
import uuid

class ProductRepository:
    def create_product(product: Product):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Inserción de los datos del objeto User en la tabla
            insert_query = """
                INSERT INTO product (id,id_owner,name,description,image,label,created_at,updated_at,stock,price,discount_price)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """

            cursor.execute(insert_query, (str(uuid.uuid4()), product.id_owner, product.name, product.description, product.image,json.dumps(product.label),datetime.now(),datetime.now(), product.stock, product.price, product.discount_price))
            
            conn.commit()

        except Exception as e:
            print(f"Error al almacenar el producto: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()
            
    def get_product(input_id_owner: str,input_name: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            if (len(input_name)>0):
                cursor.execute(("SELECT id,id_owner,name,description,image,label,created_at,updated_at,stock,price,discount_price FROM PRODUCT WHERE id_owner=%s AND name~%s ORDER BY name ASC"), (input_id_owner,input_name,))    
            else:
                cursor.execute(("SELECT id,id_owner,name,description,image,label,created_at,updated_at,stock,price,discount_price FROM PRODUCT WHERE id_owner=%s ORDER BY name ASC"), (input_id_owner,))
            
            # Obtiene todos los registros de la consulta
            records = cursor.fetchall()
                        
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()
            
             # Creo la lista
            products = []
            
            # Convierte los registros a una lista de diccionarios y retorna la lista
            for record in records:
                product ={"id": record[0], "id_owner": record[1], "name": record[2], "description": record[3], "image": record[4], "label": record[5],"created_at": record[6], "updated_at": record[7], "stock": record[8], "price": record[9], "discount_price": record[10]}
                products.append(product)
                                   
            return products
        
        except Exception as e:
            print(f"Error al listar los productos: {e}")
            
    def update_product(product: Product):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            # Actualización de los datos del objeto User en la tabla
            update_query = """
                UPDATE product SET name=%s,description=%s,image=%s,label=%s,updated_at=%s WHERE id=%s;
            """

            cursor.execute(update_query, (product.name, product.description,product.image,product.label,datetime.now(), product.id))
            
            conn.commit()

        except Exception as e:
            print(f"Error al almacenar el usuario: {e}")
        finally:
            # Cierre de la conexión a la base de datos
            cursor.close()
            conn.close()

    def delete_product(input_id_product: str):
        
        conn = get_db_connection()

        if not conn:
            print("Error al conectar con la base de datos")
            return
            
        try:
            cursor = conn.cursor()
            
            cursor.execute(("DELETE FROM PRODUCT WHERE id=%s"), (input_id_product,)) 
            
            conn.commit()
                        
            # Cierra la conexión y el cursor
            cursor.close()
            conn.close()
            
        except Exception as e:
            print(f"Error al listar los productos: {e}")