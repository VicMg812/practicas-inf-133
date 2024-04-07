import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple
query_lista = """
{
        plantas{
            id
            nombre
            especie
            edad
            altura
            frutos
        }
    }
"""
# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        plantaPorId(id: 2){
            nombre
        }
    }
"""

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)

# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        crearPlanta(nombre: "Manzana", especie: "Manzano", edad: 23,altura: 400,frutos:"Manzanas") {
            planta {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_crear})
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deletePlanta(id: 3) {
            estudiante {
                id
                nombre
                especie
                edad
                altura
                frutos
            }
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_especie = """
mutation {
        plantaPorEspecie(especie: "Manzano"){
            especie
        }
    }
"""

response_mutation = requests.post(url, json={'query': query_especie})
print(response_mutation.text)
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)
query_frutos="""
mutation{
    plantaPorFrutos(){
        nombre
    }
}
"""
response_mutation = requests.post(url, json={'query': query_frutos})
print(response_mutation.text)
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)