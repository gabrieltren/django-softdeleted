from .views import mov, mov2, MovViewSet

from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('mov', MovViewSet)

app_name = 'core'

urlpatterns = [
    path('', mov, name='movimentacao'),
    path('json/', mov2, name='rest')
]