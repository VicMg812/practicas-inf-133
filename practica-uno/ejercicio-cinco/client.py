import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
ruta_post = url + "animales"
nuevo_animal = {
    "nombre": "Leon",
    "especie": "Felino",
    "genero": "Hembra",
    "edad": 6,
    "peso": 180,
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_animal)
print(post_response.text)
# GET /animales
ruta_get = url + "animales"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#animal especie 
especie_post=url+"animales?especie=Felino"
response=requests.request(method="GET",url=especie_post)
print("son")
print(response.text)
# animal genero
genero_post=url+"animales?genero=Hembra"
response=requests.request(method="GET",url=genero_post)
print("son")
print(response.text)
# PUT actualiza un estudiante por la ruta /estudiantes
ruta_actualizar = url + "animales/1"
animal_actualizado = {
    "nombre": "Loro",
    "especie": "Canario",
    "genero":"Macho",
    "edad":7,
    "peso": 123,
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=animal_actualizado
)
print(put_response.text)
# DELETE elimina todos los estudiantes por la ruta /estudiantes
ruta_eliminar = url + "animales/1"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)
