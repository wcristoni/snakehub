from fastapi import FastAPI, HTTPException
from shared.database import get_db_connection
from shared.models import Cupom
from typing import List
import uvicorn

app = FastAPI()

@app.get("/api/cupons", response_model=List[Cupom])
def list_cupons():
    conn = get_db_connection()
    cupons = conn.execute("SELECT * FROM cupom").fetchall()
    return [dict(row) for row in cupons]

@app.get("/api/cupons/{code}", response_model=Cupom)
def get_cupom_by_code(code: str):
    
    conn = get_db_connection()
    row = conn.execute("SELECT * FROM cupom WHERE code = ?", (code,)).fetchone()
    if row:
        return dict(row)
    raise HTTPException(status_code=404, detail="Cupom não encontrado")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
