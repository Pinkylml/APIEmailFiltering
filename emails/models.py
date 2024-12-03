from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Correo(models.Model):
    destinatario = models.EmailField()
    emisor = models.EmailField()
    fecha = models.DateTimeField()
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    codigo_unico_smtp = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.emisor} -> {self.destinatario}"
