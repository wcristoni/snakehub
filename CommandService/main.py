from fastapi import FastAPI, HTTPException
from shared.database import get_db_connection
from shared.models import Cupom
import uvicorn

app = FastAPI()

@app.post("/api/cupons")
def create_cupom(cupom: Cupom):
    conn = get_db_connection()
    cursor = conn.execute("""
        INSERT INTO cupom (code, discount, type, expiration_date, usage_limit)
        VALUES (?, ?, ?, ?, ?)
    """, (
        cupom.code,
        cupom.discount,
        cupom.type,
        cupom.expiration_date.isoformat(),
        cupom.usage_limit
    ))
    conn.commit()
    return { "message": "Cupom criado com sucesso", "id": cursor.lastrowid }

@app.put("/api/cupons/{id}")
def update_cupom(id: int, cupom: Cupom):
    conn = get_db_connection()
    result = conn.execute("SELECT * FROM cupom WHERE id = ?", (id,)).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Cupom não encontrado")
    
    conn.execute("""
        UPDATE cupom SET code=?, discount=?, type=?, expiration_date=?, usage_limit=?
        WHERE id=?
    """, (
        cupom.code,
        cupom.discount,
        cupom.type,
        cupom.expiration_date.isoformat(),
        cupom.usage_limit,
        id
    ))
    conn.commit()
    return { "message": "Cupom atualizado com sucesso" }

@app.delete("/api/cupons/{id}")
def delete_cupom(id: int):
    conn = get_db_connection()
    result = conn.execute("SELECT * FROM cupom WHERE id = ?", (id,)).fetchone()
    if result is None:
        raise HTTPException(status_code=404, detail="Cupom não encontrado")
    
    conn.execute("DELETE FROM cupom WHERE id = ?", (id,))
    conn.commit()
    return { "message": "Cupom deletado com sucesso" }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8081, reload=True)
