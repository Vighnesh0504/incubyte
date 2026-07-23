from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import Vehicle
from .permissions import IsAdminUserOnly
from .serializers import VehicleSerializer
from .filters import VehicleFilter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .services import purchase_vehicle, restock_vehicle

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

class PurchaseVehicleView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, pk):

        vehicle = get_object_or_404(
            Vehicle,
            pk=pk,
        )

        try:

            vehicle = purchase_vehicle(vehicle)

            return Response(
                {
                    "message": "Vehicle purchased successfully.",
                    "quantity": vehicle.quantity,
                },
                status=status.HTTP_200_OK,
            )

        except ValueError as e:

            return Response(
                {"detail": str(e)},
                status=status.HTTP_400_BAD_REQUEST,
            )

class RestockVehicleView(APIView):

    permission_classes = [IsAdminUserOnly]

    def post(self, request, pk):

        vehicle = get_object_or_404(
            Vehicle,
            pk=pk,
        )

        amount = request.data.get("quantity")

        try:

            vehicle = restock_vehicle(
                vehicle,
                int(amount),
            )

            return Response(
                {
                    "message": "Vehicle restocked.",
                    "quantity": vehicle.quantity,
                }
            )

        except ValueError as e:

            return Response(
                {"detail": str(e)},
                status=400,
            )