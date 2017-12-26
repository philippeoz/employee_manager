"""luizalabs_employee_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

from django.conf import settings

from django.contrib import admin

from django.contrib.auth import views as auth_views

from backend.core import urls as core_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^employee/', include(core_urls)),

    # url(r'^login/', auth_views.login, name='login'),
    # url(r'^logout/', auth_views.logout_then_login,
    #     {'login_url': '/login'}, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
