"""e_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings
from django.conf import settings
from .views import(
    test_view,
    logoutTest_view,
    home_view,
    find_user_view
)
urlpatterns = [
    path('', include('account.urls')),
    path('account/', include('account.urls')),
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls')),
    path('voting/', include('voting.urls')),
    path('home/', home_view,name='home'),
    path('test/', test_view, name='test'),
    path('logoutTest/', logoutTest_view, name='logoutTest'),
    path('classify', find_user_view, name='classify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
