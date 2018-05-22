from django.conf.urls import url, include
from boot import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    url(r'^login/',views.boot_login)
]

