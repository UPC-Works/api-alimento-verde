from datetime import datetime
from modelos import User 
from repositorios.user import UserRepository

class UserService:
    def SignUp(user: User):

        try:
            UserRepository.create_user(user)
        except Exception as e:
            return {"error":"Error al intentar crear usuario","message": ""}
        finally:
            return {"error":"","message": "OK"}
    
    def SignIn(input_email: str,input_password: str):

        try:
            user = UserRepository.get_user(input_email,input_password)
            if len(user)>0:
                return {"error":"","message": user}     
            else:
                return {"error":"Este usuario no existe","message": user}
        except Exception as e:
            return {"error":"Error al intentar crear usuario","message": ""}
        
    def Update(user: User):

        try:
            user = UserRepository.update_user(user)
            return {"error":"","message": user}   
        except Exception as e:
            return {"error":"Error al intentar crear usuario","message": ""}
        
    def ListAll():

        try:
            list_users = UserRepository.get_all_users()
            return {"error":"","message": list_users}   
        except Exception as e:
            return {"error":"Error al intentar crear usuario","message": []}