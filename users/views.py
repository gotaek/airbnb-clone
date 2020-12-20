from django.views import View
from django.shortcuts import render
from . import forms

# 사용자들이 보게 될 곳


class LoginView(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
