from fastapi import FastAPI, Query, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from modelos import User,Product,Label,Schedule
from services.user import UserService
from services.product import ProductService
from services.label import LabelService
from services.schedule import ScheduleService
import shutil
import os
import uuid

app = FastAPI()

# Configurar CORS
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "null",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Acceso no autorizado"}

@app.post("/sign-up")
async def sign_up(user: User):
    return UserService.SignUp(user)

@app.post("/sign-in")
async def sign_in(user: User):
    return UserService.SignIn(user.email,user.password)

@app.put("/user/update")
async def update(user: User):
    return UserService.Update(user)

@app.get("/user")
async def list_all():
    return UserService.ListAll()

@app.post("/product")
async def add(product: Product):
    return ProductService.Add(product)

@app.get("/product/{id_owner}")
async def list_all(id_owner: str, name: str = Query(None), type_user: int = Query(None)):
    return ProductService.ListAll(id_owner,name,type_user)

@app.post("/product/upload")
async def upload_image(image: UploadFile = File(...)):
    image_extension = os.path.splitext(image.filename)[-1]
    image_id = f"{uuid.uuid4()}{image_extension}"
    saved_image_path = f'images/{image_id}'
    with open(saved_image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"error":"","message": f'D:/Github/python/github.com/Aphofisis/AlimentoVerde/api-alimento-verde/{saved_image_path}'}  

@app.delete("/product/{id_product}")
async def list_all(id_product: str):
    return ProductService.Delete(id_product)

@app.post("/label")
async def add(label: Label):
    return LabelService.Add(label)

@app.get("/label/{id_owner}")
async def list_all(id_owner: str):
    return LabelService.ListAll(id_owner)

@app.post("/schedule")
async def add(schedule: Schedule):
    return ScheduleService.Add(schedule)

@app.get("/schedule/{id_owner}")
async def list_all(id_owner: str):
    return ScheduleService.ListAll(id_owner)



