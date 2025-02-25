from fastapi import FastAPI
from datetime import datetime
import pytz

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "API de fecha funcionando"}

@app.get("/fecha")
def obtener_fecha():
    zona_horaria = pytz.timezone("UTC")  # Cambia si necesitas otra zona horaria
    fecha_actual = datetime.now(zona_horaria)
    return {"fecha": fecha_actual.isoformat()}
