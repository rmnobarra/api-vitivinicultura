# Histórias

História de Usuário 1: Como usuário da API, quero consultar os dados públicos da Embrapa para diferentes categorias de vitivinicultura, para poder consumir essas informações em aplicações externas.

Tarefas:
 
 Criar projeto base com FastAPI.

 Definir estrutura de pastas conforme boas práticas (e.g., app/, routes/, services/, models/).

 Criar rota /producao que retorne os dados de produção.

 Criar rota /processamento que retorne os dados de processamento.

 Criar rota /comercializacao que retorne os dados de comercialização.

 Criar rota /importacao que retorne os dados de importação.

 Criar rota /exportacao que retorne os dados de exportação.

 Criar modelos de dados com Pydantic para cada rota.

 Implementar lógica de scraping com requests e BeautifulSoup para cada aba.

História de Usuário 2: Como consumidor da API, quero que ela esteja bem documentada, para que eu saiba como utilizá-la facilmente.

Tarefas:

 Definir response_model em todos os endpoints.

 Adicionar docstrings e exemplos para cada modelo com Field(...) do Pydantic.

 Validar automaticamente os tipos de dados retornados.

 Verificar e validar a geração automática da documentação Swagger (/docs).

 Criar README com exemplos de uso e chamadas à API.

História de Usuário 3: Como responsável pelos dados, quero garantir que apenas usuários autorizados possam acessar certas rotas da API, para evitar uso indevido.

Tarefas:

 Implementar autenticação via JWT usando OAuth2PasswordBearer.

 Criar rota /login com credenciais de exemplo (sem persistência).

 Proteger rotas com Depends(verify_token).

 Adicionar documentação sobre como obter e usar o token JWT.

 Definir variáveis de ambiente para a SECRET_KEY.

História de Usuário 4: Como DevOps, quero disponibilizar a API em produção, para que o cliente possa testá-la e integrá-la com outros sistemas.

Tarefas:

 Escrever um arquivo requirements.txt com todas as dependências.

 Criar main.py com o objeto FastAPI e inclusão das rotas via include_router.

 Criar Procfile (Heroku) ou start.sh (Render).

 Publicar a API em uma plataforma gratuita (ex: Render, Railway ou Heroku).

 Testar o acesso externo via navegador e ferramentas como Postman.

 Compartilhar o link da API funcionando.

História de Usuário 5: Como arquiteto do sistema, quero ter um plano claro de arquitetura do projeto, para facilitar futuras integrações com bancos de dados e modelos de Machine Learning.

Tarefas:

 Criar diagrama de arquitetura com:

Site da Embrapa → Scraper → API FastAPI → (futuramente) Banco de dados → ML Model.

 Documentar fluxo de ingestão de dados e possíveis melhorias.

 Sugerir tecnologias futuras para armazenamento (ex: PostgreSQL, MongoDB).

 Incluir diagrama no repositório (como imagem ou PDF).

 Descrever um possível cenário de uso da API para modelos de ML no README.md.

História de Usuário 6: Como desenvolvedor colaborador, quero ter um repositório claro e bem documentado, para contribuir ou usar o projeto com facilidade.

Tarefas:

 Criar repositório no GitHub com nome claro e descritivo.

 Adicionar um README.md com:

Visão geral do projeto.

Instruções de instalação local.

Como rodar a aplicação localmente.

Como fazer chamadas aos endpoints.

Link para a API publicada.

 Criar um .gitignore adequado (por exemplo, com .env, __pycache__, etc.).

 Adicionar LICENSE apropriada (MIT, Apache 2.0, etc.).

 Criar pelo menos um exemplo de teste unitário com pytest.