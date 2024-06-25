from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate, logout
from django.shortcuts import render, redirect

class SignUpView(FormView):
    template_name = 'joke_app/signup.html'
    form_class = UserCreationForm
    success_url = 'home'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name = 'joke_app/login.html'
    success_url='home'

def logout_user(request):
    logout(request)
    return redirect('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'joke_app/home.html'
