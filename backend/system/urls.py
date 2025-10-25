
from django.contrib import admin
from django.urls import path,include 
from system.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Login.as_view(), name='login'),
    path('logout/',Logout.as_view(), name='logout'),
]
