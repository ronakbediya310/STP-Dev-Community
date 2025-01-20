from django.urls import path
from . import views

app_name = 'doubts'

urlpatterns = [
    path('', views.home, name='home'),
    path('doubt/<int:pk>/', views.doubt_detail, name='doubt_detail'),
    path('create/', views.create_doubt, name='create_doubt'),
]
