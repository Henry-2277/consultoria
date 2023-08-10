import sqlite3

from fastapi import FastAPI


app = FastAPI()

@app.delete("/contrato/listar/{id}")
def listar_contratos(id: int):


    banco = sqlite3.connect("tcc.db")
    cursor = banco.cursor()

    sql = f"DELETE FROM contratos WHERE id = {id}"
    cursor.execute(sql)
    banco.commit()


    cursor.close()



    return {"id": id}