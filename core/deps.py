from typing import AsyncGenerator  # Importa AsyncGenerator para tipagem de geradores assíncronos
from sqlalchemy.ext.asyncio import AsyncSession  # Importa a classe AsyncSession para sessões assíncronas
from core.dataBase import Session  # Importa a fábrica de sessões do arquivo database.py

# Função para gerenciar a criação e fechamento de sessões de forma segura
async def getSession() -> AsyncGenerator[AsyncSession, None]:
    async with Session() as session:  # Instancia e cria uma sessão de banco de dados
        try:
            yield session  # Fornece a sessão para a função chamadora
        finally:
            await session.close()  # Garante que a sessão será fechada após o uso
