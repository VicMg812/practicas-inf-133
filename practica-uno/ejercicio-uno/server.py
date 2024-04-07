from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

#Suma de numeros enteros
def suma_dos_numeros(num1, num2):
    return num1 + num2
#Resta de numeros enteros
def restar(a, b):
    return a - b
#Multiplicar de numeros enteros
def multiplicar(a, b):
    return a * b

#Division de numeros enteros
def dividir(a,b):
    # if b==0:
    #     return "Division por cero es invalido"
    return a / b

# Creamos la ruta del servidor SOAP
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)
# Nuevo endpoint para la suma de dos números
dispatcher.register_function(
    "SumaDosNumeros",
    suma_dos_numeros,
    returns={"resultado": int},
    args={"num1": int, "num2": int},
)
# Nuevo endpoint para la suma de dos números
dispatcher.register_function(
    "Restar",
    restar,
    returns={"resultado": int},
    args={"a": int, "b": int},
)
# Nuevo endpoint para la suma de dos números
dispatcher.register_function(
    "Multiplicar",
    multiplicar,
    returns={"resultado": int},
    args={"a": int, "b": int},
)
# Nuevo endpoint para la suma de dos números
dispatcher.register_function(
    "Dividir",
    dividir,
    returns={"resultado": int},
    args={"a": int, "b": int},
)
# Iniciamos el servidor HTTP
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()