import logging
import uvicorn
from fastapi import FastAPI

# Configura o logging para o projeto
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


app = FastAPI(
    title="Agente Proposta Beonne",
    description="API para crianção de uma proposta ao cliente com agente IA",
    version="0.1.0",
    docs_url="/docs"
)


@app.get("/", summary="Mensagem de status da API", tags=["Status"])
def read_root():
    return {
        "status": "success",
        "message": "Health check successful",
        "version": "0.1.0"
    }

if __name__ == "__main__":
    # Para executar: `uvicorn app.main:app --reload` a partir da raiz do projeto.
    uvicorn.run(app, host="0.0.0.0", port=8000)