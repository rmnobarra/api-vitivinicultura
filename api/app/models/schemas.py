from pydantic import BaseModel, Field
from typing import List

# --- Itens básicos ---

class ProducaoItem(BaseModel):
    produto: str = Field(..., example="Uva Isabel", description="Nome do produto vitivinícola.")
    quantidade: str = Field(..., example="123456", description="Quantidade produzida (em kg).")

class ProcessamentoItem(BaseModel):
    cultivar: str = Field(..., example="BRS Carmem", description="Nome da cultivar de uva.")
    quantidade: str = Field(..., example="98765", description="Quantidade processada (em kg).")

class ComercializacaoItem(BaseModel):
    produto: str = Field(..., example="Vinho de Mesa Tinto", description="Tipo de produto comercializado.")
    quantidade: str = Field(..., example="187016848", description="Quantidade comercializada (em litros).")

class ImportacaoItem(BaseModel):
    pais: str = Field(..., example="Chile", description="Nome do país de origem.")
    quantidade_kg: str = Field(..., example="73111416", description="Quantidade importada (em kg).")
    valor_usd: str = Field(..., example="199874777", description="Valor da importação (em dólares).")

class ExportacaoItem(BaseModel):
    pais: str = Field(..., example="Paraguai", description="Nome do país de destino.")
    quantidade_kg: str = Field(..., example="3705268", description="Quantidade exportada (em kg).")
    valor_usd: str = Field(..., example="5121857", description="Valor da exportação (em dólares).")

# --- Modelos de resposta para Swagger ---

class ProducaoResponse(BaseModel):
    ano: int = Field(..., example=2023)
    dados: List[ProducaoItem]

class ProcessamentoResponse(BaseModel):
    ano: int = Field(..., example=2023)
    dados: List[ProcessamentoItem]

class ComercializacaoResponse(BaseModel):
    ano: int = Field(..., example=2023)
    dados: List[ComercializacaoItem]

class ImportacaoResponse(BaseModel):
    ano: int = Field(..., example=2024)
    dados: List[ImportacaoItem]

class ExportacaoResponse(BaseModel):
    ano: int = Field(..., example=2024)
    dados: List[ExportacaoItem]
