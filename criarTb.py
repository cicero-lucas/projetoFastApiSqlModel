from sqlmodel import SQLModel
from core.dataBase import engine # Importa a engine do banco de dados
import models.models  # Importa todos os modelos para que 

import asyncio  # Importa a biblioteca asyncio para lidar com operações assíncronas


# Função assíncrona para criar as tabelas no banco de dados
async def create_tables() -> None:
    print("Criando tabelas...")  # Mensagem para indicar o início do processo de criação

    async with engine.begin() as conn:  # Inicia uma conexão com a engine do banco de dados
        # Drop all existing tables (caso existam)
        await conn.run_sync(SQLModel.metadata.drop_all)
        # Create all tables definidas nos modelos
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Tabelas criadas com sucesso.") 

# Ponto de entrada do script, executa a função de criação de tabelas
if __name__ == "__main__":
    asyncio.run(create_tables())  # Executa a criação de tabelas usando asyncio
