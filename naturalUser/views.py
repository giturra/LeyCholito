from django.views.generic.base import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'naturalUser/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(TemplateView):
    template_name = 'naturalUser/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

# TODO cambiar atributo body del template login