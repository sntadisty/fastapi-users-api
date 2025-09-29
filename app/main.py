# app/main.py

from fastapi import FastAPI # ⬅️ Pastikan ada impor ini

# ⬇️ OBJEK UTAMA: Variabel ini HARUS bernama 'app' 
app = FastAPI() 

# Contoh endpoint (Opsional, tapi bagus untuk verifikasi)
@app.get("/")
def home():
    return {"status": "OK"}
