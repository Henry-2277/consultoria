import sqlite3
from fastapi import APIRouter
from pydantic import BaseModel

atualizar_router = APIRouter()

# Modelo de dados para atualização do cadastro
class AtualizacaoCadastro(BaseModel):
    numero_contrato: str
    nome_prefeitura: str
    responsavel_prefeitura: str
    cnpj: str
    valor_contrato: float
    data_validade_contrato: str
    dados_pdf: str

@atualizar_router.put("/contratos/{contrato_id}")
def atualizar_contrato(contrato_id: int, dados: AtualizacaoCadastro):
    # Conectar ao banco de dados SQLite
    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    # Verificar se o contrato existe
    cursor.execute("SELECT * FROM contratos WHERE id = ?", (contrato_id,))
    contrato = cursor.fetchone()
    if contrato is None:
        return {"mensagem": "Contrato não encontrado"}

    # Atualizar o cadastro do contrato
    cursor.execute("""
        UPDATE contratos SET
        numero_contrato = ?,
        nome_prefeitura = ?,
        responsavel_prefeitura = ?,
        cnpj = ?,
        valor_contrato = ?,
        data_validade_contrato = ?,
        dados_pdf = ?
        WHERE id = ?
    """, (
        dados.numero_contrato,
        dados.nome_prefeitura,
        dados.responsavel_prefeitura,
        dados.cnpj,
        dados.valor_contrato,
        dados.data_validade_contrato,
        dados.dados_pdf,
        contrato_id
    ))

    # Salvar as alterações no banco de dados
    banco.commit()

    # Fechar a conexão com o banco de dados
    banco.close()

    return {"mensagem": "Cadastro de contrato atualizado com sucesso", "dados": dados.dict()}