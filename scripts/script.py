
from datetime import datetime
from emails.models import Empresa, Correo
import random

Correo.objects.all().delete()
Empresa.objects.all().delete()

# Crear empresas de ejemplo
empresas = [
    Empresa.objects.create(nombre="Empresa A"),
    Empresa.objects.create(nombre="Empresa B"),
    Empresa.objects.create(nombre="Empresa C"),
    Empresa.objects.create(nombre="Empresa D"),
    Empresa.objects.create(nombre="Empresa E"),
    Empresa.objects.create(nombre="Empresa F"),
    Empresa.objects.create(nombre="Empresa G"),
    Empresa.objects.create(nombre="Empresa H"),
]

# Función para generar correos aleatorios
def generar_correo(empresa):
    destinatarios = [f"destinatario{i}@dominio.com" for i in range(1, 6)]
    nombre_emp=empresa.nombre.strip().lower()
    nombre_emp=nombre_emp.replace(" ", "")
    emisores = [f"emisor{i}@{nombre_emp}.com" for i in range(1, 6)]
    contenido = f"Este es un correo de ejemplo para la empresa {empresa.nombre}"

    return Correo(
        destinatario=random.choice(destinatarios),
        emisor=random.choice(emisores),
        fecha=datetime.now(),
        empresa=empresa,
        codigo_unico_smtp=str(random.randint(1000000000, 9999999999)),
        contenido=contenido
    )

# Agregar 25 correos por cada empresa
for empresa in empresas:
    for _ in range(100):
        generar_correo(empresa).save()

print("Datos insertados exitosamente")
