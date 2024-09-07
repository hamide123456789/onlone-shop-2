from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView

from .forms import CustomUserCreationForm


class SignUpView(CreateView):
    template_name = 'registration/login.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
