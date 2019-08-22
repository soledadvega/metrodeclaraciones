from datetime import date
from django.db import models
from django.conf import settings
from django.urls import reverse
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices
from trix.fields import TrixField


class Declaracion(models.Model):
    ESTADOS = Choices('borrador', 'publicado')
    CHOICE_PLANTILLA = Choices('Soledad', 'Default')
    fecha_publicacion = MonitorField(monitor='estado', when=['publicado'], editable=False)
    cargado_por = models.ForeignKey(settings.AUTH_USER_MODEL, editable=False)
    título = models.CharField(max_length=100)
    fecha = models.DateField(default=date.today())
    declaración = TrixField()

    estado = StatusField(choices_name='ESTADOS')
    nota_interna = models.TextField(blank=True, null=True)

    opciones_plantilla = StatusField(choices_name = 'CHOICE_PLANTILLA')

    def get_absolute_url(self):
        return reverse('update', kwargs={'pk': self.pk})

    class Meta:
        ordering = ('estado', '-fecha', '-id')
