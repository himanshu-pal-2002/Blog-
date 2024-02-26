from django.urls import path,re_path
from .views import *

urlpatterns = [
    # path('register/',UserRegisterView.as_view(),name='register'),  
    path('logout/',logout_user, name='logout'),
    path('login/',login_user, name='login'),
    path('register/',register_user, name='register'),



]   