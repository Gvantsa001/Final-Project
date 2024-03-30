from django.urls import path
from . import views
from .views import EventListCreateAPIView, EventRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', views.getEvent),
    path('post/', views.postEvent),
    path('events/', EventListCreateAPIView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyAPIView.as_view(), name='event-detail'),
]