from fastapi import APIRouter, Query
from app.services.scraper import scrape_importacao
from app.models.schemas import ImportacaoResponse

from fastapi import Depends
from app.auth.dependencies import verify_token

router = APIRouter()

@router.get("/importacao", response_model=ImportacaoResponse, tags=["Importação"])
def get_importacao(ano: int = Query(2023, ge=1970, le=2023), _: str = Depends(verify_token)):
    """Retorna dados de importação de vinhos de mesa por país."""
    dados = scrape_importacao(ano)
    return {"ano": ano, "dados": dados} 
