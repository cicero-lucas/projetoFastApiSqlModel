from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings  # Importa as configurações principais

# Criação da engine assíncrona usando a URL do banco de dados definida nas configurações
engine = create_async_engine(settings.DB_URL, echo=True)

# Configuração do sessionmaker para criar sessões assíncronas
Session: AsyncSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False
)
