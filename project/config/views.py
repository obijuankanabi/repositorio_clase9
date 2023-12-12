from django.http import HttpResponse

def saludo(request):
    return HttpResponse("¡Hola!")

# Crear una función que solicite mi nombre
# y la muestre en pantalla al ingresar a una url
# diferente a 'saludo'

def saludo2(request) -> HttpResponse:
    nombre = input('Ingresa tu nombre')
    return HttpResponse(f'Tu nombre es {nombre}')