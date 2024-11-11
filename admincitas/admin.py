from django.contrib import admin
from admincitas.models import Paciente
from admincitas.models import Medico
from admincitas.models import Cita
from admincitas.models import Historial

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cita)
admin.site.register(Historial)
