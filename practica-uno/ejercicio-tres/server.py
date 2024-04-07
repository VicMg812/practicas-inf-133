from http.server import HTTPServer, BaseHTTPRequestHandler
import json

from urllib.parse import urlparse, parse_qs

pacientes=[
    {
        "ci":6864853,
        "nombre":"Pedro",
        "apellido":"Mamani",
        "edad":23,
        "genero":"Masculino",
        "diagnostico":"Fractura",
        "doctor":"Juan"
    },
]

class PacientesService:
    @staticmethod
    def crea_paciente(data):
        data["ci"]=len(pacientes)+1
        pacientes.append(data)
        return pacientes

    @staticmethod
    def busca_paciente(ci):
        return next(
            (paciente for paciente in pacientes if paciente["ci"]==ci),
            None,
        )

    @staticmethod
    def lista_diagnostico(diagnostico):
        return [
            paciente for paciente in pacientes if paciente["diagnostico"]== diagnostico
        ]

    @staticmethod
    def lista_doctor(doctor):
        return [
            paciente for paciente in pacientes if paciente["doctor"]== doctor
        ]  
    
    @staticmethod
    def actualizar_paciente(ci, data):
        paciente = PacientesService.busca_paciente(ci)
        if paciente:
            paciente.update(data)
            return pacientes
        else:
            return None

    @staticmethod
    def borrar_paciente():
        pacientes.clear()
        return pacientes

class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

class RESTRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path=="/pacientes":
            if "diagnostico" in query_params:
                diagnostico=query_params["diagnostico"][0]
                paciente_filtrado=PacientesService.lista_diagnostico(diagnostico)
                if paciente_filtrado !=[]:
                    HTTPResponseHandler.handle_response(
                        self,200,paciente_filtrado
                    )
                else:
                    HTTPResponseHandler.handle_response(self,204,[])
            # else:
            #     HTTPResponseHandler.handle_response(self,200,pacientes)
            elif "doctor" in query_params:
                doctor=query_params["doctor"][0]
                pacientedoc_filtrado=PacientesService.lista_doctor(doctor)
                if pacientedoc_filtrado !=[]:
                    HTTPResponseHandler.handle_response(
                        self,200,pacientedoc_filtrado
                    )
                else:
                    HTTPResponseHandler.handle_response(self,204,[])
            else:
                HTTPResponseHandler.handle_response(self,200,pacientes)
        elif self.path.startswith("/pacientes/"):
            ci=int(self.path.split("/")[-1])
            paciente=PacientesService.busca_paciente(ci)
            if paciente:
                HTTPResponseHandler.handle_response(self,200,[paciente])
            else:
                HTTPResponseHandler.handle_response(self,204,[])
        else:
            HTTPResponseHandler.handle_response(
                self,204,{"Error":"Ruta no existente"}
            )
    def do_POST(self):
        if self.path=="/pacientes":
            data=self.read_data()
            pacientes=PacientesService.crea_paciente(data)
            HTTPResponseHandler.handle_response(self,201,pacientes)
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    def do_PUT(self):
        if self.path.startswith("/pacientes/"):
            ci=int(self.path.split("/")[-1])
            data=self.read_data()
            pacientes=PacientesService.actualizar_paciente(ci,data)
            if pacientes:
                HTTPResponseHandler.handle_response(self,200,pacientes)
            else:
                HTTPResponseHandler.handle_response(
                    self ,404,{"Error":"Paceinte no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    def do_DELETE(self):
        if self.path=="/pacientes":
            pacientes=PacientesService.borrar_paciente()
            HTTPResponseHandler.handle_response(self,200,pacientes)
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    def read_data(self):
        content_length=int(self.headers["Content-Length"])
        data=self.rfile.read(content_length)
        data=json.loads(data.decode("utf-8"))
        return data
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()