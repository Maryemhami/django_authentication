from django.urls import path,include
from . import views

urlpatterns = [
    path('register/user/', views.RegisterUser.as_view(),name="register"),
    path('login/', views.LoginView.as_view(), name="login"),
   
]
