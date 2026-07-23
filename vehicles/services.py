from django.db import transaction
from django.db.models import F

from .models import Vehicle


def purchase_vehicle(vehicle: Vehicle):

    with transaction.atomic():

        vehicle = (
            Vehicle.objects
            .select_for_update()
            .get(id=vehicle.id)
        )

        if vehicle.quantity == 0:
            raise ValueError("Vehicle is out of stock.")

        vehicle.quantity = F("quantity") - 1

        vehicle.save()

        vehicle.refresh_from_db()

        return vehicle

def restock_vehicle(vehicle: Vehicle, amount: int):

    if amount <= 0:
        raise ValueError(
            "Restock quantity must be greater than zero."
        )

    with transaction.atomic():

        vehicle = (
            Vehicle.objects
            .select_for_update()
            .get(id=vehicle.id)
        )

        vehicle.quantity = F("quantity") + amount

        vehicle.save()

        vehicle.refresh_from_db()

        return vehicle