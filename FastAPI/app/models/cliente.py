from pydantic import BaseModel

class Clientes(BaseModel): 
    id_         : int
    nome        : str
    email       : str
    telefone    : str

class ClienteCriarAtualizar(BaseModel):
    nome        : str
    email       : str
    telefone    : str


