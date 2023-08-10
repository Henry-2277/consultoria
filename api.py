
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


from Listar_Contratos import listar_router
from Inserir_Contratos import inserir_router
from Excluir_Contrato_id import excluir_router
from Atualizar_Contrato_id import atualizar_router
from Baixar_pdf import baixarpdf_router
from login import

app = FastAPI()
app.include_router(baixarpdf_router)
app.include_router(excluir_router)
app.include_router(listar_router)
app.include_router(inserir_router)
app.include_router(atualizar_router)


# Configurando o CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitindo todas as origens. Você pode ajustar para permitir origens específicas.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# # class Contrato extends Basemodel
#
# # API DE CADASTRO DE CONTRATO
# class Contrato(BaseModel):
#     # type hints - tipagem fraca pra ensinar o pythonn
#     # variavel: tipo
#     # diferente de variavel = valor
#     # pode usar em conjunto varivel: tipo = valor  ----- String nome = "Igor"
#     id: int | None
#     numero_contrato: str
#     nome_prefeitura: str
#     responsavel_prefeitura: str
#     cnpj: str
#     valor_contrato: float
#     data_validade_contrato: str
#     dados_pdf: str

# # def soma(x1: int, x2: int)
#
# @app.post("/contrato/inserir")
# def inserir_contrato(contrato: Contrato):
#
#     #prova de que a função e a rota recebeu os dados
#     #print(contrato.id)
#     #print(contrato.numero_contrato)
#     # print(contrato.nome_empresa)
#     # print(contrato.data_contrato)
#     # print(contrato.dados_pdf)
#
#     # api precisa enviar os dados para o banco
#     enviar_dados_banco(
#         numeroC=contrato.numero_contrato,
#         nomePref=contrato.nome_prefeitura,
#         responsavelPref=contrato.responsavel_prefeitura,
#         cnpj=contrato.cnpj,
#         valorC=contrato.valor_contrato,
#         dataValidadeC=contrato.data_validade_contrato,
#         pdf=contrato.dados_pdf
#     )
#
#     return {
#         "Contrato cadastrado com sucesso"
#     }
#
# def enviar_dados_banco(numeroC, nomePref, responsavelPref, cnpj, valorC, dataValidadeC, pdf):
#     # prova de que a funcao recebeu os dados
#     #print(numeroC, nomePref, responsavelPref, cnpj,  valorC, dataValidadeC, pdf)
#
#     #cria conexao com banco
#     banco = sqlite3.connect("tcc.db")
#     cursor = banco.cursor()
#
#     try:
#         # cria a SQL de insert
#         sql = f"INSERT INTO contratos('numero_contrato','nome_prefeitura','responsavel_prefeitura','cnpj', 'valor_contrato', 'data_validade_contrato', 'dados_pdf' ) VALUES ('{numeroC}', '{nomePref}', '{responsavelPref}', '{cnpj}', {valorC}, '{dataValidadeC}', '{pdf}')"
#         cursor.execute(sql)
#         banco.commit()
#         print("DADOS SALVO NO BANCO")
#
#     except:
#         banco.rollback()
#         print("OCORREU UM ERRO AO SALVAR")
#
#     # # cria a SQL de insert
#     # sql = f"INSERT INTO contratos('numero_contrato','nome_empresa','data_contrato','dados_pdf') VALUES ({numero}, '{nome_empresa}', '{data}', '{pdf}')"
#     # cursor.execute(sql)
#     # banco.commit()
#     # print("DADO SALVO NO BANCO")
#
#
#
#
#
# #@app.post("/contrato/inserir") fiz
#
# #@app.get("/contrato/listar") fiz
#
# #@app.get("/contrato/listar/{id}") não fiz
#
# #@app.delete("/contrato/excluir/{id}") fiz
#
# #@app.put("/contrato/atualizar/{id}") não fiz
# #def atualizar_contrato(contrato: Contrato)
#
#
# import sqlite3
# from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# class Contrato(BaseModel):
#
#     id: int | None
#     numero_contrato: str
#     nome_prefeitura: str
#     responsavel_prefeitura: str
#     cnpj: str
#     valor_contrato: float
#     data_validade_contrato: str
#     dados_pdf: str
#
#
# # @app.post("/contrato/inserir")
# # def inserir_contrato(contrato: Contrato):
# #
# #     enviar_dados_banco(
# #         numeroC=contrato.numero_contrato,
# #         nomePref=contrato.nome_prefeitura,
# #         responsavelPref=contrato.responsavel_prefeitura,
# #         cnpj=contrato.cnpj,
# #         valorC=contrato.valor_contrato,
# #         dataValidadeC=contrato.data_validade_contrato,
# #         pdf=contrato.dados_pdf
# #     )
# #
# #     return {
# #         "Contrato cadastrado com sucesso"
# #     }
# #
# # def enviar_dados_banco(numeroC, nomePref, responsavelPref, cnpj, valorC, dataValidadeC, pdf):
# #
# #     banco = sqlite3.connect("tcc.db")
# #     cursor = banco.cursor()
# #
# #     try:
# #         sql = f"INSERT INTO contratos('numero_contrato','nome_prefeitura','responsavel_prefeitura','cnpj', 'valor_contrato', 'data_validade_contrato', 'dados_pdf' ) VALUES ('{numeroC}', '{nomePref}', '{responsavelPref}', '{cnpj}', {valorC}, '{dataValidadeC}', '{pdf}')"
# #         cursor.execute(sql)
# #         banco.commit()
# #         print("DADOS SALVO NO BANCO")
# #
# #     except:
# #         banco.rollback()
# #         print("OCORREU UM ERRO AO SALVAR")
#
#
#
#
#
# @app.get("/contrato/listar")
# def listar_contratos():
#
#     banco = sqlite3.connect("tcc.db")
#     cursor = banco.cursor()
#
#     sql = f"SELECT * FROM contratos"
#     cursor.execute(sql)
#
#     contratos = cursor.fetchall()
#
#
#     registros = []
#     for contrato in contratos:
#         registro = {
#
#             "id": contrato[0],
#             "numero_contrato":contrato[1],
#             "nome_prefeitura": contrato[2],
#             "responsavel_prefeitura": contrato[3],
#             "cnpj": contrato[4],
#             "valor_contrato": contrato[5],
#             "data_validade_contrato": contrato[6],
#             "dados_pdf": contrato[7]
#         }
#
#         registros.append(registro)
#
#
#
#     # Fecha a conexão com o banco de dados
#     cursor.close()
#
#     # Retorna a lista de registros em formato JSON
#     return {'registro': registros}
#
#
#
#
#
# @app.delete("/contrato/deletar/{id}")
# def deletar_contratos(id: int):
#
#
#     banco = sqlite3.connect("tcc.db")
#     cursor = banco.cursor()
#
#     sql = f"DELETE FROM contratos WHERE id = {id}"
#     cursor.execute(sql)
#     banco.commit()
#
#
#     cursor.close()
#
#
#
#     return {"id": id}
#
#
#
#
#
#
#
#
#
