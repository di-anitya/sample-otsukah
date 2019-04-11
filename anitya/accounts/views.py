from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login

from accounts.models import User
from accounts.forms import SignUpForm


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'accounts/signup.html'
    #success_url = reverse_lazy('accounts:index')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        login(self.request, self.object)

        return response
