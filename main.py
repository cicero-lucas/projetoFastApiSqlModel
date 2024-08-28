from fastapi import FastAPI
from core.config import settings
import uvicorn

from api.v1.api import appRouter as routerFilmes

# Inicialização da aplicação FastAPI
app = FastAPI()

# Inclusão do roteador, usando o prefixo definido nas configurações
app.include_router(routerFilmes, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    # Executando o servidor Uvicorn com o aplicativo FastAPI
    uvicorn.run('main:app', host="127.0.0.1", port=8000, log_level="info", reload=True)
