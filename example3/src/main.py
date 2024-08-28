from fastapi import FastAPI

from typing import Optional

from math import pi

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Wellcome Maguila! ¬¬ "}


@app.get("/meu-pi")
def meu_pi():
    return {"número pi" : pi }


@app.get("/gritos_/")
@app.get("/gritos_/{grito_id}")
def read_item(grito_id: Optional[int] = None):     
    gritos = {0 : "Cawabanga", 1 : "Ghostbusters", 2 : "Vilmaaaaa", 3 : "Hadouken"}
    if grito_id is None:
        return gritos
           
    result = gritos.get(grito_id)    
    return result if result else "Esse grito não foi encontrado."
            