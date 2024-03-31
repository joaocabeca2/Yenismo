import json
import os
'''
the college dropout
graduation
ye
my beautiful dark twisted fantasy
the life of pablo
yeezus
808s & heartbreak
donda
watch the throne
'''

def add_album():
    nome_album = input('\nQual o nome do album que você quer adicionar?').lower()
    api_dict[nome_album] = {}

def criar_musica():
    nome_musica = input('Qual nome da musica que você quer adicionar?').lower()
    api_dict[nome_album][nome_musica] = []

with open('api.json','r') as api:
    api_dict = json.load(api)


def mostrar_albuns():  
    for x in range(len(lista_de_albuns)):
        print(x+1,'-',lista_de_albuns[x])

def mostrar_musicas():
    for x in range(len(lista_de_musicas)):
        print(x+1,'-',lista_de_musicas[x])

def mostrar_frases():
    for frase in api_dict[nome_album][nome_musica]:
        print(frase)
        
while True:
    os.system('cls')

    lista_de_albuns = [album for album in api_dict]
    mostrar_albuns()

    indice_album = int(input('\nQual album?'))
    try:
        nome_album = lista_de_albuns[indice_album-1]
    except IndexError:
        add_album()
        continue
    
    os.system('cls')

    lista_de_musicas = [musica for musica in api_dict[nome_album]]
    mostrar_musicas()

    indice_musica = int(input('\nQual musica?'))
    try:
        nome_musica = lista_de_musicas[indice_musica-1]
    except IndexError:
        criar_musica()
        continue

    os.system('cls')
    
    mostrar_frases()
    frase = input('\nQual frase?\n').lower()
    api_dict[nome_album][nome_musica].append(frase)

    continuar = input('\nQuer adicionar mais?\n')
    if continuar != 's' and continuar != 'sim':
        break

with open('api.json','w') as api:
    json.dump(api_dict,api)

  


