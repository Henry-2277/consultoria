import sqlite3
from fastapi import APIRouter, Response

baixarpdf_router = APIRouter()

@baixarpdf_router.get("/contratos/{contrato_id}/pdf")
def baixar_pdf(contrato_id: int):
    # Conectar ao banco de dados SQLite
    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    # Verificar se o contrato existe
    cursor.execute("SELECT dados_pdf FROM contratos WHERE id = ?", (contrato_id,))
    contrato = cursor.fetchone()
    if contrato is None:
        return {"mensagem": "Contrato não encontrado"}

    # Fechar a conexão com o banco de dados
    banco.close()

    # Extrair o conteúdo em base64 do resultado da consulta
    base64_pdf = contrato[0]

    # Decodificar o base64 para obter os dados binários do PDF
    import base64
    pdf_binario = base64.b64decode(base64_pdf)

    # Configurar a resposta do arquivo
    response = Response(content=pdf_binario, media_type="application/pdf")

    # Definir o nome do arquivo e o cabeçalho para download
    response.headers["Content-Disposition"] = f"attachment; filename=contrato_{contrato_id}.pdf"

    # Retornar a resposta do arquivo
    return response
