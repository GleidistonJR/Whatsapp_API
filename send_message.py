import requests


BASE_URL = 'http://localhost:8080'
INSTANCE_NAME = 'chave_store'
EVOLUTION_AUTHENTICATION_API_KEY = 'MakkersBR'

MENSAGEM = '''
Hellow word
'''

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    'number': '5547988037520',
    'text': MENSAGEM,
    'delay': 1000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)

print(response.json())