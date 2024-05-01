from django.urls import path
from .views import main_view, logout_view

urlpatterns = [
    path('', main_view, name='main'),
    path('logout/', logout_view, name='logout'),
]

