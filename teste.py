import requests
import json
import smtplib
from email.message import EmailMessage
from keys import LINK,LOGIN,SENHA,HEADERS,DESTINATARIOS

'''content = requests.get('http://127.0.0.1:8000/frase')

content = json.loads(content.text)
print(content)'''


def gerar_citacao_ye():
    response = requests.get(LINK, headers=HEADERS)
    response_json = json.loads(response.text) #frase
    return f'\n{response_json[2]}\nAlbum: {response_json[0]}\nMusica: {response_json[1]}'


mensagem = EmailMessage()
mensagem['Subject'] = 'Uma frase de Kanye West para melhorar seu dia!'
mensagem['From'] = LOGIN

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as servidor:
  servidor.login(LOGIN, SENHA)
  for email in DESTINATARIOS:
    mensagem['To'] = email
    mensagem.set_content(gerar_citacao_ye())
    servidor.send_message(mensagem)
    del mensagem['To']
