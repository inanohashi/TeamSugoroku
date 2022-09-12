from django.http import HttpResponse
from django.views.generic import TemplateView

class sign_up_Class(TemplateView):
    template_name = 'sign_up.html'

class sign_in_Class(TemplateView):
    template_name = 'sign_in.html'