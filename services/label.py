from datetime import datetime
from modelos import Label 
from repositorios.label import LabelRepository

class LabelService:
    def Add(label: Label):

        try:
            LabelRepository.create_label(label)
        except Exception as e:
            return {"error":"","message": "Error al intentar crear la etiqueta"}
        finally:
            return {"error":"","message": "OK"}
    def ListAll(input_id_owner: str):

        try:
            list_label = LabelRepository.get_label(input_id_owner)
            return {"error":"","message":list_label}
        except Exception as e:
            return {"error":"Error al intentar crear producto","message": []}
        finally:
            return {"error":"","message": []}
