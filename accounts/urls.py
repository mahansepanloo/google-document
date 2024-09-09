from django.urls import path
from . import views



app_name = "account"
urlpatterns = [

    path('login',views.Login.as_view(),name="login"),
    path('refresh', views.Login.as_view(), name="Refresh"),
    path('sign', views.SingIN.as_view(), name="sign"),

]
