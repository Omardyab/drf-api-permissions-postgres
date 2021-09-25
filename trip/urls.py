from django.urls import path
from .views import TripsList, TripsDetail

urlpatterns = [
    path('', TripsList.as_view(), name='trips_list'),
    path('<int:pk>/', TripsDetail.as_view(), name='trips_detail'),
]