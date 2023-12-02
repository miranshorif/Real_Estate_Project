from django.urls import path
from .views import ContactSerializerView
urlpatterns = [
    path('',ContactSerializerView.as_view(),name='contact'),
]
