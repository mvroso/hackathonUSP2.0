from django.conf.urls import url
from django.urls import include, path
from . import views

# We are adding a URL called /home
urlpatterns = [
    path('', views.home, name='home'),
]
