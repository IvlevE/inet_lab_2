"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from main import IndexView, BlogView, ConfirmationView, CartView, CheckView, ContactView, CategoryView, LoginView, \
    RegisterView, SingleView, ProdView, OrderView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('index/', IndexView.as_view(), name='index'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('cart/', include('cart.urls', namespace='cart')),
    # path('cart/', CartView.as_view(), name='cart'),
    path('category/', CategoryView.as_view(), name='category'),
    path('checkout/', CheckView.as_view(), name='checkout'),
    path('confirmation/', ConfirmationView.as_view(), name='confirmation'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('single-blog/', SingleView.as_view(), name='single-blog'),
    path('single-product/<int:pk>/', ProdView.as_view(), name='single-product'),
    path('admin/', admin.site.urls),
    path('tracking-order/', OrderView.as_view(), name='tracking-order')
]
