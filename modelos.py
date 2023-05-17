from pydantic import BaseModel
from typing import Optional,List, Dict
from datetime import datetime
from datetime import time

class User(BaseModel):
    id: Optional[str]
    full_name: Optional[str]
    password: Optional[str]
    email: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    id_type: Optional[int]
    status: Optional[bool]

class Product(BaseModel):
    id: Optional[str]  
    id_owner: str
    name: str
    description: str
    image: str
    label: Optional[List[Dict]]
    stock: int
    price: float
    discount_price: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
    
class Schedule(BaseModel):
    id_owner: str
    id_day: int
    start_hour: time
    end_hour: time
    available: bool

class DaySchedule(BaseModel):
    id: int
    name: str

class Label(BaseModel):
    id: str
    id_owner:str
    name: str
























