from django.urls import path
from api.views.ContainerView import ContainerView
from api.views.ProductView import ProductView
from api.views.ClientView import ClientView
from api.views.UserView import UserView
from api.views.TruckView import TruckView
from api.views.LoginView import LoginView, LogOutView


urlpatterns = [
    path('container/', ContainerView.as_view(), name='container_list'),
    path('container/<str:id>', ContainerView.as_view(), name='container_process'),
    path('product/', ProductView.as_view(), name='product_list'),
    path('product/<str:id>', ProductView.as_view(), name='product_process'),
    path('client/', ClientView.as_view(), name='product_list'),
    path('client/<str:id>', ClientView.as_view(), name='product_process'),
    path('user/', UserView.as_view(), name='user'),
    path('user/<str:id>', UserView.as_view(), name='user_list'),
    path('register/user/', UserView.as_view(), name='user_register'),
    path('login/', LoginView.as_view(), name='login'),
    path('truck/', TruckView.as_view(), name='truck'),
    path('truck/<str:id>', TruckView.as_view(), name='trucks')
]
