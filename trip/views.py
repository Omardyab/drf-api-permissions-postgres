from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Trip
from .serializers import TripSerializer

class TripsList(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripsDetail(RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
