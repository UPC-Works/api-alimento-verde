from datetime import datetime
from modelos import Product 
from repositorios.product import ProductRepository

class ProductService:
    def Add(product: Product):
        try:
            ProductRepository.create_product(product)
        except Exception as e:
            return {"error":"","message": "Error al intentar crear producto"}
        finally:
            return {"error":"","message": "OK"}

    def ListAll(input_id_owner: str,input_name: str,input_type_user: int):
        if input_type_user==1:
            try:
                list_product = ProductRepository.get_product(input_id_owner,input_name,input_type_user)
                return {"error":"","message":list_product}
            except Exception as e:
                return {"error":"Error al intentar crear producto","message": []}
        else:
            try:
                list_product = ProductRepository.get_product(input_id_owner,input_name,input_type_user)
                return {"error":"","message":list_product}
            except Exception as e:
                return {"error":"Error al intentar crear producto","message": []}    
    def Delete(input_id_product: str):
        try:
            list_product = ProductRepository.delete_product(input_id_product)
            return {"error":"","message": "OK"}
        except Exception as e:
            return {"error":"","message": "Error al intentar eliminar el producto"}