from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import ContactForm
from .telegramm import send_message


class LeadCreationView(CreateView):
    form_class = ContactForm
    # success_url = reverse_lazy('callback')
    success_url = '/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        phone = form.cleaned_data['phone']
        message = "*ЗАЯВКА С САЙТА*:" + "\n" + "*ИМЯ*: " +str(name) + "\n" + "*ТЕЛЕФОН*: " + str(phone)
        send_message(message)
        return super(LeadCreationView, self).form_valid(form)

    def form_invalid(self, form):
        return redirect(self.get_success_url())