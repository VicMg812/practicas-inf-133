from zeep import Client

client=Client('http://localhost:8000')
suma = client.service.SumaDosNumeros(num1=5,num2=1)
resta = client.service.Restar(a=8, b=2)
multiplicacion= client.service.Multiplicar(a=2, b=4)
# dividir= client.service.Dividir(a=6, b=2)
print(suma)
print(resta)
print(multiplicacion)
# print(dividir)