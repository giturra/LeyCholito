from .forms import ComplaintForm
from django.views.generic.edit import FormView


class ComplaintFormView(FormView):
    template_name = 'complaint/complaint_form.html'
    form_class = ComplaintForm

    def get(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)



