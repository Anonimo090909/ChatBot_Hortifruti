"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from chatbot_loja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'),
    path('chatbot/', views.pagina_chatbot, name='chatbot'),
    path('responder-chatbot/', views.responder_chatbot, name='responder_chatbot'),
    path('finalizar-compra/', views.finalizar_compra, name='finalizar_compra'),
    path('confirmar-pedido/', views.confirmar_pedido, name='confirmar_pedido'),
    path('acompanhar-pedido/', views.acompanhar_pedido, name='acompanhar_pedido'),
]

