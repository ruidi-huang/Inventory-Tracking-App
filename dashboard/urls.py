from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'dashboard-index'), 
    path('product/', views.product, name= 'dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name= 'dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name= 'dashboard-product-update'),
    path('export', views.export_users_csv, name='export_users_csv'),
]
