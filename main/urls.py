from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index,name='index'),
    path('groop-register', views.groop_register,name='groop_register')

]
