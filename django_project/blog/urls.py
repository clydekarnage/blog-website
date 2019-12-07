from django.urls import path
from . import views  # .(dot) means I imported it from the same directory

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog-about"),
]
