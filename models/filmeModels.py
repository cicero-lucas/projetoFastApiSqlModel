from typing import Optional
from sqlmodel import Field, SQLModel

class FilmeModel(SQLModel, table=True):
    __tablename__ : str = "filmes"  # Nome da tabela no banco de dados

    id: Optional[int] = Field(default=None, primary_key=True)  # ID do filme
    titulo: str  # Título do filme
    autor: str  # Autor do filme
    duracao: float  # Duração do filme
