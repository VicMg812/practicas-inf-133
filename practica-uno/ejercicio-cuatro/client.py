import requests

url = "http://localhost:8000/pacientes"
headers = {'Content-type': 'application/json'}

# Crear paciente  
mi_paciente = {
    "ci": "6864853",
    "nombre": "Victor",
    "apellido": "Medina",
    "edad":"20",
    "genero":"Masculino",
    "diagnostico":"Fractura",
    "doctor": "Jose",
}
response = requests.post(url, json=mi_paciente, headers=headers)
print(response.json())

# Listar Pacientes
response = requests.get(url)
print(response.json())


# Actualizar paciente
edit_paciente = {
    "ci": "6864853",
    "nombre": "Ruben",
    "apellido": "Mamani",
    "edad":"28",
    "genero":"Masculino",
    "diagnostico":"Sangrado",
    "doctor": "Jose",
}
response = requests.put(url+'/1', json=edit_paciente, headers=headers)
print(response.json())


#diagnostico diabetes
response=requests.get(url+"/diagnostico/Sangrado")
print("El paciente es:")
print(response.json())

# buscar por ci
response=requests.get(url+"/ci/6864853")
print("El paciente por ci es:")
print(response.json())


#diagnostico doctor
response=requests.get(url+"/doctor/Jose")
print("El paciente es:")
print(response.json())

# eliminar paciente

response = requests.delete(url + "/1")
print(response.json())

