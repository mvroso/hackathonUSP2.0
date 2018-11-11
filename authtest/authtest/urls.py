"""authtest URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
# Add this import
from django.contrib.auth import views
from django.urls import include, path
from log.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('log.urls')),
    path('login/', views.login, kwargs={'template_name': 'login.html', 'authentication_form': LoginForm}),
    # url(r'^logout/$', views.logout, {'next_page': '/login'}),
]
