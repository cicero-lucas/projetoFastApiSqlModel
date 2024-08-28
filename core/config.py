
from pydantic_settings import BaseSettings

# Classe que define as configurações principais da aplicação
class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "mysql+asyncmy://root:@localhost:3306/cinemaDb"  # URL de conexão com o banco de dados MySQL

    class Config:
        case_sensitive = True

# Instância das configurações
settings = Settings()
