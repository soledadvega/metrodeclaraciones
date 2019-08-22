from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.views.generic import edit
from .models import Declaracion
from .forms import DeclaracionForm

from django_weasyprint import WeasyTemplateResponseMixin


class BaseView(LoginRequiredMixin):
    model = Declaracion
    form_class = DeclaracionForm
    template_name = 'base.html'


class ListView(BaseView, generic.ListView):
    template_name = 'declaracion/list.html' # 'declaracion/list.html'
    paginate_by = 10


class CreateView(BaseView, edit.CreateView):
    template_name = 'declaracion/form.html'

    def form_valid(self, form):
        messages.info(self.request, 'Declaración «{}» creada correctamente'.format(form.instance.título))
        form.instance.cargado_por = self.request.user
        return super(CreateView, self).form_valid(form)


class UpdateView(BaseView, edit.UpdateView):
    template_name = 'declaracion/form.html'

    def form_valid(self, form):
        messages.info(self.request, 'Declaración «{}» modificada correctamente'.format(form.instance.título))
        return super(UpdateView, self).form_valid(form)


class DeclaracionHTML(generic.DetailView):
    model = Declaracion

    def get_template_names(self):
        objeto = self.get_object()
        if objeto.opciones_plantilla == 'Soledad':
            return ['declaracion/declaracion2.html']
        else:
            return ['declaracion/declaracion.html']







class DeclaracionPDF(WeasyTemplateResponseMixin, DeclaracionHTML):
    pass


class DeclaracionPNG(DeclaracionPDF):
    '''
    content_type = 'image/png' #sacamos
    '''
