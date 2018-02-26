from django.views.generic.base import TemplateView
from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'naturalUser/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


