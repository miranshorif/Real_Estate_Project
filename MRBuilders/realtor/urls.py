from django.urls import path
from .views import AgentDetailView,AgentListView,TopSellerListView

urlpatterns = [
    path('',AgentListView.as_view(),name='agentlist'),
    path('<pk>/',AgentDetailView.as_view(),name='agentdetails'),
    path('topseller',TopSellerListView.as_view(),name='topseller'),
]

