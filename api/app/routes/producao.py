from fastapi import APIRouter, Query
from app.services.scraper import scrape_producao
from app.models.schemas import ProducaoResponse

from fastapi import Depends
from app.auth.dependencies import verify_token



router = APIRouter()

@router.get("/producao", response_model=ProducaoResponse, tags=["Produção"])
def get_producao(ano: int = Query(2023, ge=1970, le=2023), _: str = Depends(verify_token)):
    """Retorna dados de produção vitivinícola do RS."""
    dados = scrape_producao(ano)
    return {"ano": ano, "dados": dados} 
