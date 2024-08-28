from fastapi import APIRouter

from api.v1.endpoints.filmeEndpoints import router as filmeRouter

appRouter = APIRouter()

# Incluindo o roteador para as rotas relacionadas a cursos
appRouter.include_router(filmeRouter, prefix="/filmes", tags=["filmes"])
