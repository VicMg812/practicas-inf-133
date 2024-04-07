import requests
import json

url = "http://localhost:8000/animales"
headers = {"Content-Type": "application/json"}

# Crear un animal (POST /animales)
new_animal_data = {
    "animal_type": "mamifero",
    "nombre": "Pulga",
    "especie": "Canino",
    "genero": "Macho",
    "edad": 5,
    "peso": 20
}
response = requests.post(url=url, json=new_animal_data, headers=headers)
print(response.json())

new_animal_data = {
    "animal_type": "ave",
    "nombre": "Lucas",
    "especie": "Canario",
    "genero": "Macho",
    "edad": 8,
    "peso": 5
}
response = requests.post(url=url, json=new_animal_data, headers=headers)
print(response.json())
# Listar todos los animales (GET /animales)
response = requests.get(url=url)
print(response.json())

# Buscar animales por especie (GET /animales?species={especie})
especie_to_search = "Canino"
response = requests.get(f"{url}?especie={especie_to_search}")
print("El animal de especie es:")
print(response.json())

# Buscar animales por género (GET /animales?gender={genero})
genero_to_search = "Macho"
response = requests.get(f"{url}?genero={genero_to_search}")
print("El animal de genero es:")
print(response.json())

# Actualizar la información de un animal (PUT /animales/{id})
animal_id_to_update = 1
updated_animal_data = {
    "nombre": "Algodon",
    "edad": 6
}
response = requests.put(f"{url}/{animal_id_to_update}", json=updated_animal_data)
print("Animal actualizado:", response.json())

# Eliminar un animal (DELETE /animales/{id})
animal_id_to_delete = 1
response = requests.delete(f"{url}/{animal_id_to_delete}")
print("Animal eliminado:", response.json())

# Listar todos los animales después de eliminar uno (GET /animales)
response = requests.get(url=url)
print(response.json())