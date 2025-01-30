from django.contrib import admin
from django.urls import path, include  # Correct import
from accounts import urls as accounts_urls  # Import accounts app urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(accounts_urls)),  # Include accounts URLs here
]
