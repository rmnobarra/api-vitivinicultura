from fastapi import APIRouter, Query
from app.services.scraper import scrape_exportacao
from app.models.schemas import ExportacaoResponse

from fastapi import Depends
from app.auth.dependencies import verify_token


router = APIRouter()

@router.get("/exportacao", response_model=ExportacaoResponse, tags=["Exportação"])
def get_exportacao(ano: int = Query(2023, ge=1970, le=2023), _: str = Depends(verify_token)):
    """Retorna dados de exportação de vinhos de mesa por país."""
    dados = scrape_exportacao(ano)
    return {"ano": ano, "dados": dados} 
