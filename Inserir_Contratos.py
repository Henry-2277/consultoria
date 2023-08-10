import sqlite3
from fastapi import APIRouter
from pydantic import BaseModel

inserir_router = APIRouter()

# class Contrato extends Basemodel

# API DE CADASTRO DE CONTRATO
class Contrato(BaseModel):
    # type hints - tipagem fraca pra ensinar o pythonn
    # variavel: tipo
    # diferente de variavel = valor
    # pode usar em conjunto varivel: tipo = valor  ----- String nome = "Igor"

    id: int | None = None
    numero_contrato: str
    nome_prefeitura: str
    responsavel_prefeitura: str
    cnpj: str
    valor_contrato: float
    data_validade_contrato: str
    dados_pdf: str

# def soma(x1: int, x2: int)

@inserir_router.post("/contrato/inserir")
def inserir_contrato(contrato: Contrato):

    #prova de que a função e a rota recebeu os dados
    #print(contrato.id)
    #print(contrato.numero_contrato)
    # print(contrato.nome_empresa)
    # print(contrato.data_contrato)
    # print(contrato.dados_pdf)

    # api precisa enviar os dados para o banco
    enviar_dados_banco(
        numeroC=contrato.numero_contrato,
        nomePref=contrato.nome_prefeitura,
        responsavelPref=contrato.responsavel_prefeitura,
        cnpj=contrato.cnpj,
        valorC=contrato.valor_contrato,
        dataValidadeC=contrato.data_validade_contrato,
        pdf=contrato.dados_pdf
    )

    return {
        "Contrato cadastrado com sucesso"
    }

def enviar_dados_banco(numeroC, nomePref, responsavelPref, cnpj, valorC, dataValidadeC, pdf):
    # prova de que a funcao recebeu os dados
    #print(numeroC, nomePref, responsavelPref, cnpj,  valorC, dataValidadeC, pdf)

    #cria conexao com banco
    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    try:
        # cria a SQL de insert
        sql = f"INSERT INTO contratos('numero_contrato','nome_prefeitura','responsavel_prefeitura','cnpj', 'valor_contrato', 'data_validade_contrato', 'dados_pdf' ) VALUES ('{numeroC}', '{nomePref}', '{responsavelPref}', '{cnpj}', {valorC}, '{dataValidadeC}', '{pdf}')"
        cursor.execute(sql)
        banco.commit()
        print("DADOS SALVO NO BANCO")

    except:
        banco.rollback()
        print("OCORREU UM ERRO AO SALVAR")

    # # cria a SQL de insert
    # sql = f"INSERT INTO contratos('numero_contrato','nome_empresa','data_contrato','dados_pdf') VALUES ({numero}, '{nome_empresa}', '{data}', '{pdf}')"
    # cursor.execute(sql)
    # banco.commit()
    # print("DADO SALVO NO BANCO")