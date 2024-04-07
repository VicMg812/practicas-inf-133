import requests

# Consultando a un servidor RESTful
url = "http://localhost:8000/"
# POST agrega un nuevo estudiante por la ruta /estudiantes
ruta_post = url + "pacientes"
nuevo_paciente = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "edad":15,
    "genero":"Masculino",
    "diagnostico": "Anemia",
    "doctor":"Ben",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_paciente)
print(post_response.text)
# GET obtener a todos los estudiantes por la ruta /estudiantes
ruta_get = url + "pacientes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#Buscar estudiante
buscar_get=url+"pacientes/2"
bus_response=requests.request(method="GET",url=buscar_get)
print("Paciente buscado")
print(bus_response.text)

#lista pacientes con diagnostico
dig_get=url+"pacientes?diagnostico=Fractura"
diagnostico_response=requests.request(method="GET",url=dig_get)
print("El paciente es:")
print(diagnostico_response.text)

#lista pacientes con el doctor 
doc_get=url+"pacientes?doctor=Ben"
doctor_response=requests.request(method="GET",url=doc_get)
print("El doctor es:")
print(doctor_response.text)

#actualizar paciente
actu_paciente=url+"pacientes/2"
actualizar_paciente={
    "nombre":"Jose",
}
post_response=requests.request(method="GET",url=actu_paciente,json=actualizar_paciente)
print("Paciente Actualizado")
print(post_response.text)
#Delete
ruta_delete=url+"pacientes/2"
delete_response=requests.request(method="GET",url=ruta_delete)
print("Paciente eliminado:")
print(delete_response.text)
