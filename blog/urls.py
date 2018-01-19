from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'tests', views.TestView)

urlpatterns = [
    path('', views.index, name='index'),
    path('/random', views.random, name='random'),
    path('router/', include(router.urls))
]