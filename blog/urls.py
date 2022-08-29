from .views import posts

from django.urls import path

app_name = 'blog'


urlpatterns = [
    path('', posts, name="Posts")
]