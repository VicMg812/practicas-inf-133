from http.server import HTTPServer, BaseHTTPRequestHandler
import json

animales={}
class Animal:
    def __init__(self,animal_type,nombre,especie,genero,edad,peso):
        self.animal_type = animal_type
        self.nombre = nombre
        self.especie = especie
        self.genero = genero
        self.edad = edad
        self.peso = peso

class Mamifero(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__("mamifero", nombre, especie, genero, edad, peso)
class Ave(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__("ave", nombre, especie, genero, edad, peso)
class Reptil(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__("reptil", nombre, especie, genero, edad, peso)
class Anfibio(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__("anfibio", nombre, especie, genero, edad, peso)
class Pez(Animal):
    def __init__(self, nombre, especie, genero, edad, peso):
        super().__init__("pez", nombre, especie, genero, edad, peso)

class AnimalFactory:
    @staticmethod
    def crea_animal(animal_type,nombre,especie,genero,edad,peso):
        if animal_type=="mamifero":
            return Mamifero(nombre,especie,genero,edad,peso)
        elif animal_type=="ave":
            return Ave(nombre,especie,genero,edad,peso)
        elif animal_type=="reptil":
            return Reptil(nombre,especie,genero,edad,peso)
        elif animal_type=="anfibio":
            return Anfibio(nombre,especie,genero,edad,peso)
        elif animal_type=="pez":
            return Pez(nombre,especie,genero,edad,peso)
        else:
            raise ValueError("Tipo de animal no válido")

class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))

class AnimalService:
    def __init__(self):
        self.factory = AnimalFactory()
    def add_animal(self, data):
        animal_type = data.get("animal_type", None)
        nombre = data.get("nombre", None)
        especie = data.get("especie", None)
        genero = data.get("genero", None)
        edad = data.get("edad", None)
        peso = data.get("peso", None)

        animal = self.factory.crea_animal(
            animal_type, nombre, especie, genero, edad, peso
        )
        animales[len(animales) + 1] = animal
        return animal

    def list_animals(self):
        return {index: animal.__dict__ for index, animal in animales.items()}

    def search_animals_by_species(self, especie):
        return {
            index: animal.__dict__
            for index, animal in animales.items()
            if animal.especie == especie
        }

    def search_animals_by_gender(self, genero):
        return {
            index: animal.__dict__
            for index, animal in animales.items()
            if animal.genero == genero
        }

    def update_animal(self, animal_id, data):
        if animal_id in animales:
            animal = animales[animal_id]
            for key, value in data.items():
                setattr(animal, key, value)
            return animal
        else:
            return None

    def delete_animal(self, animal_id):
        if animal_id in animales:
            del animales[animal_id]
            return {"message": "Animal eliminado"}
        else:
            return None

class AnimalRequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.animal_service = AnimalService()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/animales":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.animal_service.add_animal(data)
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/animales":
            response_data = self.animal_service.list_animals()
            HTTPDataHandler.handle_response(self, 200, response_data)
        elif self.path.startswith("/animales?especie="):
            species = self.path.split("=")[-1]
            response_data = self.animal_service.search_animals_by_species(species)
            HTTPDataHandler.handle_response(self, 200, response_data)
        elif self.path.startswith("/animales?genero="):
            gender = self.path.split("=")[-1]
            response_data = self.animal_service.search_animals_by_gender(gender)
            HTTPDataHandler.handle_response(self, 200, response_data)
        elif self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            if animal_id in animales:
                response_data = animales[animal_id].__dict__
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Animal no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.animal_service.update_animal(animal_id, data)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Animal no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/animales/"):
            animal_id = int(self.path.split("/")[-1])
            response_data = self.animal_service.delete_animal(animal_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Animal no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, AnimalRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()