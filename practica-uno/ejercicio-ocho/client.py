import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# POST agrega un nuevo estudiante por la ruta /mensaje
ruta_post = url + "mensajes"
nuevo_mensaje = {
    "contenido(mensaje a encriptar)": "Juanito",
    "contenido encriptado": "Mxdplwr",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_mensaje)
print(post_response.text)
# GET obtener a todos los estudiantes por la ruta /mensaje
ruta_get = url + "mensajes"
get_response = requests.request(method="GET", url=ruta_get)
print("Mensajes")
print(get_response.text)
#Buscar estudiante
buscar_get=url+"mensajes/2"
bus_response=requests.request(method="GET",url=buscar_get)
print("Mensaje buscado")
print(bus_response.text)
#actualizar paciente
actu_mensaje=url+"mensajes/2"
actualizar_mensaje={
    "contenido(mensaje a encriptar)":"Jose",
}
post_response=requests.request(method="GET",url=actu_mensaje,json=actualizar_mensaje)
print("Mensaje Actualizado")
print(post_response.text)
#Delete mensaje
ruta_delete=url+"mensajes/2"
delete_response=requests.request(method="GET",url=ruta_delete)
print("Mensaje eliminado:")
print(delete_response.text)