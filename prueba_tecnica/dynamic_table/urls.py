from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet, basename='producto')

urlpatterns = [
    path('', views.main, name='main'),
    path('product_form/', views.product_form, name='product_form'),
    path('edit_form/<int:id>', views.edit_form, name='edit_form'),
    path('delete/<int:id>', views.delete_data, name='delete'),
    path('api/', include(router.urls)),
]