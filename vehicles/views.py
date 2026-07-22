from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Vehicle
from .permissions import IsAdminUserOnly
from .serializers import VehicleSerializer


class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = Vehicle.objects.all().order_by("-created_at")

    serializer_class = VehicleSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUserOnly()]

        return [IsAuthenticated()]