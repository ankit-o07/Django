from django.urls import path ,include
from .views import home , login_view , sigup_view , logout_view ,addTodo ,delete ,status ,update

urlpatterns = [
    path('', home , name="Home"),
    path('login/', login_view , name="login"),
    path('signup/',sigup_view, name='signup'),
    path('logout/',logout_view, name="logout"),
    path('addTodo/',addTodo , name='AddTodo'),
    path('delete/<int:id>', delete,name="del" ),
    path('status/<int:id>/<str:st>',status,name="status"),
    path('update/<>int:id',update,name="update")

]