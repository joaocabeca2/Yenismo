from fastapi import FastAPI
from random import choice
import json

app = FastAPI()

@app.get('/')
def homepage():
    with open(file='api.json',mode='r') as jsonfile:
        return json.load(jsonfile)

@app.get('/frase')
def pegar_frase_aleatoria():
    with open('api.json','r') as jsonfile:
        api_ye = json.load(jsonfile)
        album_aleatorio = choice(list(api_ye.items()))[0]
        musica_aleatoria = choice(list(api_ye[album_aleatorio].items()))[0]
        return (album_aleatorio,musica_aleatoria,choice(api_ye[album_aleatorio][musica_aleatoria]))
