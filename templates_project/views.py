from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

class sign_up_Class(TemplateView):
    template_name = 'sign_up.html'

class sign_in_Class(TemplateView):
    template_name = 'sign_in.html'

    

def errorview(request):
    errormesage = "パスワードが正しくありません"
    return render(request, 'error.html', {'errormessage':errormesage})