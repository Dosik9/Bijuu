from django.shortcuts import render, redirect
from django.urls import reverse #, reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model

# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from .forms import SimpleUserForm
# from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth import logout
from django.views.generic.base import View

# class registerView(CreateView):
#     form_class = SimpleUserForm
#     success_url = 'signIn'
#     template_name = 'registration.html'
#     def reg_message(request):
#         messages.success(request, f'Account created for {username}!')
#
#     def form_valid(self, form):
#             # Создаём пользователя, если данные в форму были введены корректно.
#             form.save()
#             username = form.cleaned_data.get('username')
#             # Вызываем метод базового класса
#             return super(registerView, self).form_valid(form)
#
def profile(request):
    
    return render(request, "user_page.html")

def register(request):
    if request.method == 'POST':
        form=SimpleUserForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Account created for {username}!')
            return redirect('/')
    else:
        form = SimpleUserForm()
    return render(request, 'registration.html', {
                                                 'form': form
    })

class LoginFormView(FormView):
    form_class = AuthenticationForm

        # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "signIn.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)



class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")
    # Redirect to a success page.
# def signIn(request):
# #     if request.method == 'POST':
# #         form=SimpleUserForm(request.POST)
# #         template
#     return render(request, 'signIn.html')

# class RegisterFormView(FormView):
#     form_class = UserCreationForm
#
#     # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
#     # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
#     success_url = "/signIn/"
#
#     # Шаблон, который будет использоваться при отображении представления.
#     template_name = "registration.html"
#
#     def form_valid(self, form):
#         # Создаём пользователя, если данные в форму были введены корректно.
#         form.save()
#
#         # Вызываем метод базового класса
#         return super(RegisterFormView, self).form_valid(form)



# def register(request):
#     if request.method == 'POST':
#         form=SimpleUserForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             success_url = "signIn"
#     else:
#         form=SimpleUserForm()
#     return render(request, "registration.html", {'form':form})
