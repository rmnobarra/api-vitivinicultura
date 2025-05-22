from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import producao, processamento, comercializacao, importacao, exportacao, auth
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Instância principal
app = FastAPI(title="API Vitivinicultura Embrapa")

# Incluir rotas
app.include_router(producao.router)
app.include_router(processamento.router)
app.include_router(comercializacao.router)
app.include_router(importacao.router)
app.include_router(exportacao.router)
app.include_router(auth.router)

from fastapi.openapi.utils import get_openapi

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description=(
            "Esta API fornece dados sobre a vitivinicultura no Brasil.\n\n"
            "### Autenticação via OAuth2:\n"
            "1. Clique em **Authorize** acima\n"
            "2. Informe `admin` / `1234` como usuário e senha\n"
            "3. Após login, o token será usado automaticamente nas rotas protegidas"
        ),
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2Password": {
            "type": "oauth2",
            "flows": {
                "password": {
                    "tokenUrl": "/login",
                    "scopes": {}
                }
            }
        }
    }

    # Aplicar segurança em todas as rotas (ou selecione só as privadas)
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"OAuth2Password": []})

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
