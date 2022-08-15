from .views import mov

from django.urls import path

app_name = 'core'

urlpatterns = [
    path('', mov, name='movimentacao')
]