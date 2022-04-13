from unicodedata import name
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('formDatabase', views.formDatabase, name='formDatabase'),
    path('login', views.login, name="login"),
    path('loginCheck', views.loginCheck, name="loginCheck")
]