from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle
from .permissions import IsAdminUserOnly
from .serializers import VehicleSerializer
from .filters import VehicleFilter

class VehicleListCreateView(generics.ListCreateAPIView):

    queryset = Vehicle.objects.all().order_by("-created_at")
    serializer_class = VehicleSerializer

    def get_permissions(self):

        if self.request.method == "POST":
            return [IsAdminUserOnly()]

        return [IsAuthenticated()]


class VehicleDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Vehicle.objects.all()

    serializer_class = VehicleSerializer

    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsAdminUserOnly()]

class VehicleSearchView(generics.ListAPIView):

    serializer_class = VehicleSerializer

    queryset = Vehicle.objects.all()

    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend]

    filterset_class = VehicleFilter