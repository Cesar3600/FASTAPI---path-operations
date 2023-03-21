
from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel,Field
from typing import Optional

app = FastAPI()
app.title = 'Mi aplicacion con fastAPI'
app.version = '0.0.1'

class Movie(BaseModel):
    id: Optional[int] = None
    title:str = Field( min_length=5, max_length=15)
    overview:str= Field(min_length=15, max_length=35)
    year: int = Field( le=2022)
    ranking:float = Field(le=10)
    category:str= Field( max_length=33)
    class Config:
        schema_extra = {
            "example":{
            "id":1,
            "title":"Mi pelicula",
            "overview":"Descripcion de la pelicula",
            "year":2022,
            "ranking":5.0,
            "category":"Comedy"
            }
        }



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
      "overview":"Una nave carguero recibe una senal de auxilio acudiendo en ayuda sin imaginar que alguien mas abordara ",
      "year":1977,
      "ranking":8.3,
      "category":"Terror"
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
def create_movie(movie:Movie):
    movies.append(movie)
    return movies

@app.put('/movies/{id}', tags=['movies'])
def update_movie(id:int, movie:Movie):
    for item in movies:
        if item['id'] == id:
            item['title'] = movie.title
            item['overview'] = movie.overview
            item['year'] = movie.year
            item['ranking'] = movie.ranking
            item['category'] = movie.category

    return movies

@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id:int):
    for movie in movies:
        if movie["id"] == id:
            movies.remove(movie)

    return movies
    




#@app.put('/movies/{id}', tags=['movies'])




