from datetime import datetime
from modelos import Schedule
from repositorios.schedule import ScheduleRepository

class ScheduleService:
    def Add(schedule: Schedule):

        try:
            ScheduleRepository.delete_schedule(schedule)
            ScheduleRepository.create_schedule(schedule)
        except Exception as e:
            return {"error":"","message": "Error al intentar crear el horario"}
        finally:
            return {"error":"","message": "OK"}
    def ListAll(input_id_owner: str):

        try:
            list_product = ScheduleRepository.get_schedule(input_id_owner)
            return {"error":"","message":list_product}
        except Exception as e:
            return {"error":"Error al intentar crear producto","message": []}
        finally:
            return {"error":"","message": []}
