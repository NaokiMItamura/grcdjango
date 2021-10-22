from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.helloworldfunction),
    path('nice/', views.helloworldfunction),

]