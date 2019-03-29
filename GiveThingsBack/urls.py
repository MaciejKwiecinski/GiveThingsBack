"""GiveThingsBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from give.views import main,SignIn,ProductView,QuantityView,OrganizationView,AddressView,EditView
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('',main),
    path('form1/',ProductView.as_view()),
    path('form2/',QuantityView.as_view()),
    path('form4/',OrganizationView.as_view()),
    path('form5/',AddressView.as_view()),
    path('form6/',EditView.as_view()),
    path('signin/',SignIn.as_view())
]