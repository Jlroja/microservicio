from django.db import models

class Paciente(models.Model):
    paciente_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Medico(models.Model):
    medico_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cita(models.Model):
    ESTADOS = [
        ('asignada', 'Asignada'),
        ('modificada', 'Modificada'),
        ('cancelada', 'Cancelada')
    ]
    cita_id = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita {self.cita_id} - {self.estado}"

class Historial(models.Model):
    ACCIONES = [
        ('creacion', 'Creación'),
        ('modificacion', 'Modificación'),
        ('cancelacion', 'Cancelación')
    ]
    historial_id = models.AutoField(primary_key=True)
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    accion = models.CharField(max_length=20, choices=ACCIONES)
    fecha_accion = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Historial {self.historial_id} - {self.accion}"