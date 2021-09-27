from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Trip
from .serializers import TripSerializer
from .permissions import IsOwnerOrReadOnly
class TripsList(ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsOwnerOrReadOnly,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
