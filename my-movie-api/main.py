
from fastapi import FastAPI

app = FastAPI()
app.title = 'Mi aplicacion con fastAPI'
app.version = '0.0.1'


@app.get('/',tags=['home'])
def message():
    return 'Hola mundo =) '


