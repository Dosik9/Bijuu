from django.urls import path
from . import views

app_name= 'Users'
urlpatterns = [
               path('signIn', views.LoginFormView.as_view(), name= 'signIn'),
               # path('register', views.registerView.as_view(), name="register"),
               path("user/", views.profile, name="profile"),
               path("logout", views.LogoutView.as_view(), name="logout"),
    # path('signIn', views.signIn, name='signIn'),
                path('register', views.register, name="register"),
    # path('register', views.RegisterFormView.as_view(), name='register')
]
