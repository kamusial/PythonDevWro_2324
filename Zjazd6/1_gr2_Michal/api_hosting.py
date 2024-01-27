"""
Żeby to zadziałało:
pip install fastapi
pip install uvicorn
uvicorn api_hosting:app
"""

from fastapi import FastAPI


app = FastAPI()


@app.get("/users")
def glowna():
    return {"imie": "Michal"}
