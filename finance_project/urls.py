from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finance_app.urls')),  # Make sure this line is correct
]
