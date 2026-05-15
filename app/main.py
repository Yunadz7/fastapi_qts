from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def raiz():
    return {"mensagem" : "API FastAPI Funcionando."}

@app.get("/healt")
def healt():
    return {"status": "ok"}

@app.get("/soma")
def soma(a: int, b: int):
    return{"resultado": a + b}

from pydantic import BaseModel
class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False

@app.post("/tarefas")
def criar_tarefa(tarefa : Tarefa):
    return {
        "mensagem": "Tarefa recebida com sucesso",
        "dados" : tarefa
    }