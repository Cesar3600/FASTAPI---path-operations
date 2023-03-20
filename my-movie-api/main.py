
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'Mi aplicacion con fastAPI'
app.version = '0.0.1'

movies = [
    {
      "id":1,
      "title":"Avatar",
      "overview":"En un exuberante planeta llamado Pandora viven los Na'vi, seres que aparentan ser primitivos pero que en realidad son muy evolucionados. Debido a que el ambiente de Pandora es venenoso, los híbridos humanos/Na'vi, llamados Avatares, están relacionados con las mentes humanas, lo que les permite moverse libremente por Pandora. Jake Sully, un exinfante de marina paralítico se transforma a través de un Avatar, y se enamora de una mujer Na'vi.",
      "year":2009,
      "ranking":7.8,
      "category":"Accion"
    },
    {
      "id":2,
      "title":"Stargate",
      "overview":"Un equipo de militares y un científico parten hacia un planeta desconocido a través de una puerta estelar descubierta en una excavación en Egipto.",
      "year":1994,
      "ranking":6.3,
      "category":"Aventura"
    },
    {
      "id":3,
      "title":"Alien",
      "overview":"Un equipo de militares y un científico parten hacia un planeta desconocido a través de una puerta estelar descubierta en una excavación en Egipto.",
      "year":2003,
      "ranking":6.3,
      "category":"Aventura"
    },
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1><p>hey hey hey !!!</p>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id:int):
    #return list(filter(lambda movie: movie['id'] == id, movies))
    return [movie for movie in movies if movie["id"]==id]

@app.get('/movies/',tags=['movies'])
def get_movies_by_category(category:str,year:str):
    #return [movie for movie in movies if movie['category'] == category]
    return list(filter(lambda movie: movie["category"] == category and movie["year"] == year, movies))


@app.post('/movies',tags=['movies'])
def create_movie(id:int = Body(), title:str=Body(), overview:str=Body(), year:int=Body(), ranking:float=Body(), category:str=Body()):
    movies.append({
        "id":id,
        "title":title,
        "overview":overview, 
        "year":year,
        "ranking":ranking,
        "category":category
    })
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id:int, title:str=Body(), overview:str=Body(), year:int=Body(), ranking:float=Body(), category:str=Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['ranking'] = ranking,
            item['category'] = category,








