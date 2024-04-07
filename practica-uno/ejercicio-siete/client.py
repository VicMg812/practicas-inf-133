import requests

url = "http://localhost:8000/"

# Crear una partida
response = requests.request(method="POST", url=url + "partidas", json={"elemento": "tijera"})
print("Partida creada:", response.json())

# Listar todas las partidas
response = requests.request(method="GET", url=url + "partidas")
print("Todas las partidas:", response.json())

# Listar partidas perdidas
response = requests.request(method="GET", url=url + "partidas?resultado=perdió")
print("Partidas perdidas:", response.json())

# Listar partidas ganadas
response = requests.request(method="GET", url=url + "partidas?resultado=ganó")
print("Partidas ganadas:", response.json())