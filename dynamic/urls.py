from django.urls import path
from . import views

urlpatterns = [
    path('branches', views.branch, name='branches'),
    path('packersandmovers/<str:city>', views.city_pages, name='city_pages'),
    path('quotation-request', views.quotation, name='quotation'),
]
