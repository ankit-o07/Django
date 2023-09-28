
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index ,name="ShopHome"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact, name="ContactUS"),
    path('tracker/',views.tracker, name="TrackerStatus"),
    path('search/',views.search, name="Search"),
    path('products/<int:myid>',views.products,name="prodview"),
    path('checkout/',views.checkout, name="Checkout"),
    
     
]
