import sqlite3
from fastapi import APIRouter

excluir_router = APIRouter()

@excluir_router.delete("/contrato/deletar/{id}")
def deletar_contratos(id: int):


    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    sql = f"DELETE FROM contratos WHERE id = {id}"
    cursor.execute(sql)
    banco.commit()
    cursor.close()
    return {"id": id}