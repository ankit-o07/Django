
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('patientApp.urls')),
    path("account/",include("accountApp.urls")),
    path("blog/",include("blogApp.urls")),
    path("lab/",include("labApp.urls")),
    path("pharmacy/",include("pharmacyApp.urls")),
    path("doctor/",include("doctorApp.urls")),
]
