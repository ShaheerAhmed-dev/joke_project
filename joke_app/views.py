from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,authenticate, logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
import requests


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
    
    def get_success_url(self):
        return reverse_lazy('login')
    
class UserLoginView(LoginView):
    template_name = 'joke_app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'joke_app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        joke = self.request.session.get('joke')
        if not joke:
            response = requests.get('https://official-joke-api.appspot.com/random_joke')
            joke = response.json()
            self.request.session['joke'] = joke
        context['joke'] = joke
        return context
    
class NewJokeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        response = requests.get('https://official-joke-api.appspot.com/random_joke')
        joke = response.json()
        request.session['joke'] = joke
        return redirect('/jokeapp/home')
