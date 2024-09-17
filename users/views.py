from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView  
from users.forms import LoginUserForm
from .forms import RegisterForm
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'title': 'Авторизация'}

    def get_success_url(self) -> str:
        return reverse_lazy('home')

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

def logout_view(request):
    logout(request)
    return redirect('home')
