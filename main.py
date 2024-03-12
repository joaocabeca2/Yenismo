import json
import requests
import smtplib
from deep_translator import GoogleTranslator
from email.message import EmailMessage
from keys import HEADERS, LINK, LOGIN, SENHA, DESTINATARIOS


def gerar_citacao_ye():
  response = requests.get(LINK, headers=HEADERS)
  frase = response.json()['quote']
  tradutor = GoogleTranslator(source='en', target='pt')
  return tradutor.translate(frase)

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
