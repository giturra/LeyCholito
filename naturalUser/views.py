from django.views.generic.base import TemplateView
from .forms import RegisterNaturalUserForm
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'naturalUser/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class LoginView(TemplateView):
    template_name = 'naturalUser/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class RegisterFormView(TemplateView):
    template_name = 'naturalUser/register.html'
    form = RegisterNaturalUserForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form})