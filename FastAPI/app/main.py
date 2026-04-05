from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.rotas import cliente
app = FastAPI(
    title="Techlog Solutions API",
    description="CRM para tecnologia e soluções de software",
    version="1.0.0",
)
app.include_router(cliente.router)

@app.get("/health")
async def health_check():
    return{"status": "API is running"}
@app.get("/front", response_class=HTMLResponse)
async def front_page():
    html_content = """
    <html>
        <head>
            <title>Techlog Solutions</title>
        </head>
        <body>
            <h1>🔪 Techlog Solutions</h1>
            <p>Sistema de Gestão de Ordens de Serviço</p>
            <p>Status: <strong>Operacional</strong></p>
        </body>
    </html>
    """
    return html_content
