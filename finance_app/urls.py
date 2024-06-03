from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet
from . import views

router = DefaultRouter()
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = [
    path('', include(router.urls)),
    path('export/', views.export_companies, name='export-companies'),

]
