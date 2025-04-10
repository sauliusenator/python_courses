from django.urls import path
from . import views
urlpatterns = [
    path('', views.prekiu_sarasas, name='prekiu_sarasas'),
    path('nauja/', views.nauja_preke, name='nauja_preke'),
    path('redaguoti/<int:pk>/', views.redaguoti_preke, name='redaguoti_preke'),
    path('istrinti/<int:pk>/', views.IstrintiPreke.as_view(), name='istrinti_preke'),  # Pakeista į klasės view
]