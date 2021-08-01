from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('pokemon', views.PokemonViewSet)
app_name = 'pokemon'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('pokemon/<int:pk>/', views.Detalhe.as_view(), name='detalhe'),
    path('api/', include(router.urls)),
]

