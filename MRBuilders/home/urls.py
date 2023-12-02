from django.urls import path
from .views import HomeDetailListView,HomeListView,ImageView,Search

urlpatterns = [
    path('',HomeListView.as_view(),name='home'),
    path('search/',Search.as_view(),name='search'),
    path('<slug>/',HomeDetailListView.as_view(),name='home_detail'),
    path('images/<pk>/',ImageView.as_view(),name='images'),
]
