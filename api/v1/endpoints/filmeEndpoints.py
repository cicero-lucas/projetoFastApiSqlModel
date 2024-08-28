from typing import List  # Importa List para tipagem de listas
from fastapi import APIRouter, Depends, HTTPException, status, Response  # Importa classes e funções do FastAPI
from sqlalchemy.ext.asyncio import AsyncSession  # Importa a classe AsyncSession para sessões assíncronas
from sqlmodel import select  # Importa a função select para consultas no banco de dados

from models.filmeModels import FilmeModel  # Importa o modelo FilmeModel
from core.deps import getSession  # Importa a dependência de sessão

router = APIRouter()  # Cria um roteador de API para agrupar as rotas relacionadas a filmes

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=FilmeModel)
async def create_filme(filme: FilmeModel, db: AsyncSession = Depends(getSession)):
    """
    Rota para criar um novo filme.
    """
    novo_filme = FilmeModel(titulo=filme.titulo, autor=filme.autor, duracao=filme.duracao)
    db.add(novo_filme)
    await db.commit()
    await db.refresh(novo_filme)
    return novo_filme

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[FilmeModel])
async def read_filmes(db: AsyncSession = Depends(getSession)):
    """
    Rota para obter a lista de todos os filmes.
    """
    query = select(FilmeModel)
    resultado = await db.execute(query)
    filmes: List[FilmeModel] = resultado.scalars().all()
    
    if filmes:
        return filmes
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nenhum filme encontrado")


@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=FilmeModel)
async def read_filme_by_id(id: int, db: AsyncSession = Depends(getSession)):
    """
    Rota para obter um filme pelo ID.
    """
    query = select(FilmeModel).where(FilmeModel.id == id)
    resultado = await db.execute(query)
    filme: FilmeModel = resultado.scalar_one_or_none()
    
    if filme:
        return filme
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_filme(id: int, db: AsyncSession = Depends(getSession)):
    """
    Rota para deletar um filme pelo ID.
    """
    query = select(FilmeModel).where(FilmeModel.id == id)
    resultado = await db.execute(query)
    filme: FilmeModel = resultado.scalar_one_or_none()
    
    if filme:
        await db.delete(filme)
        await db.commit()
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Filme {id} não encontrado")

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=FilmeModel)
async def update_filme(id: int, filme_update: FilmeModel, db: AsyncSession = Depends(getSession)):
    """
    Rota para atualizar as informações de um filme pelo ID.
    """
    query = select(FilmeModel).where(FilmeModel.id == id)
    resultado = await db.execute(query)
    filme: FilmeModel = resultado.scalar_one_or_none()
    
    if filme:
        filme.titulo = filme_update.titulo
        filme.autor = filme_update.autor
        filme.duracao = filme_update.duracao
        await db.commit()
        await db.refresh(filme)
        return filme
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Filme não encontrado")
