from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProdukViewSet
from . import views

router = DefaultRouter()
router.register(r'produk', ProdukViewSet)

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('tambah/', views.produk_tambah, name='produk_tambah'),
    path('edit/<int:pk>/', views.produk_edit, name='produk_edit'),
    path('hapus/<int:pk>/', views.produk_hapus, name='produk_hapus'),
]
