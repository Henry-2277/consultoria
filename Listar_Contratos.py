import sqlite3

from fastapi import APIRouter

listar_router = APIRouter()



@listar_router.get("/contrato/listar")
def listar_contratos():

    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    sql = f"SELECT * FROM contratos"
    cursor.execute(sql)

    contratos = cursor.fetchall()


    registros = []
    for contrato in contratos:
        registro = {

            "id": contrato[0],
            "numero_contrato":contrato[1],
            "nome_prefeitura": contrato[2],
            "responsavel_prefeitura": contrato[3],
            "cnpj": contrato[4],
            "valor_contrato": contrato[5],
            "data_validade_contrato": contrato[6],
            "dados_pdf": contrato[7]
        }

        registros.append(registro)



    # Fecha a conexão com o banco de dados
    cursor.close()

    # Retorna a lista de registros em formato JSON
    return {'registro': registros}