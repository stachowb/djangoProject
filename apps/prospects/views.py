from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.forms import UserCreationForm


class HomeView(TemplateView):
    template_name = "base.html"


class UserCreationView(FormView):
    form_class = UserCreationForm
    template_name = "register.html"