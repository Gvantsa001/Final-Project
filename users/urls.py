from django.urls import path
from .views import RegisterAPI, LoginAPI
from django.urls import path
from .views import CreateEventRetrieveUpdateDestroyAPIView,CreateEventCreateAPIView


urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('createvents/', CreateEventCreateAPIView.as_view(), name='blogpost-list-create'),
    path('createvents/<int:pk>/', CreateEventRetrieveUpdateDestroyAPIView.as_view(), name='blogpost-detail'),
]