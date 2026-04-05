from typing import Annotated


from fastapi import APIRouter,Depends,HTTPException

from app.models.cliente import Clientes , ClienteCriarAtualizar
from app.dependencias import obter_cliente_repositorio

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)
cliente_list = [Clientes(id_=1, nome="João Silva", email="joao.silva@example.com", telefone="(11) 99999-9999"),
                    Clientes(id_=2, nome="Maria Oliveira", email="maria.oliveira@example.com", telefone="(11) 88888-8888"),
                    Clientes(id_=3, nome="Carlos Santos", email="carlos.santos@example.com", telefone="(11) 77777-7777")]

@router.get("/" , response_model=list[Clientes])
async def listar_clientes(cliente_repositorio: Annotated[Clientes, Depends(obter_cliente_repositorio)]):
    return await cliente_repositorio.listar_clientes()
   

@router.get("/{cliente_id}", response_model=Clientes | None)
async def obter_cliente(cliente_repositorio: Annotated[Clientes, Depends(obter_cliente_repositorio)],
                        cliente_id: int):
    cliente = await cliente_repositorio.obter_cliente(cliente_id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente
@router.post("/", response_model=Clientes,status_code=201)
async def criar_cliente(
    cliente_repositorio: Annotated[Clientes, Depends(obter_cliente_repositorio)],
    cliente: ClienteCriarAtualizar):
    return await cliente_repositorio.criar_cliente(cliente)
@router.put("/{cliente_id}", response_model=Clientes | None)
async def atualizar_cliente(
    cliente_repositorio: Annotated[Clientes, Depends(obter_cliente_repositorio)],
    cliente_id: int,
    cliente_atualizado: ClienteCriarAtualizar):
    cliente_atualizado = await cliente_repositorio.atualizar_cliente(cliente_id, cliente_atualizado)
    if not cliente_atualizado:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente_atualizado
@router.delete("/{cliente_id}", status_code=204)
async def deletar_cliente(
    cliente_repositorio: Annotated[Clientes, Depends(obter_cliente_repositorio)],
    cliente_id: int):
    sucesso = await cliente_repositorio.deletar_cliente(cliente_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    