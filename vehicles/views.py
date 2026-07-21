from rest_framework import generics

from .models import Vehicle
from .permissions import IsAdminUserOnly
from .serializers import VehicleSerializer


class VehicleCreateView(generics.CreateAPIView):

    queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer

    permission_classes = [IsAdminUserOnly]