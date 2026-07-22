import pytest

from vehicles.models import Vehicle


@pytest.mark.django_db
def test_purchase_vehicle(user_client):

    vehicle = Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )

    response = user_client.post(
        f"/api/vehicles/{vehicle.id}/purchase/"
    )

    assert response.status_code == 200

    vehicle.refresh_from_db()


    assert vehicle.quantity == 4

@pytest.mark.django_db
def test_cannot_purchase_out_of_stock(user_client):

    vehicle = Vehicle.objects.create(
        make="BMW",
        model="X5",
        category="SUV",
        price=50000,
        quantity=0,
    )

    response = user_client.post(
        f"/api/vehicles/{vehicle.id}/purchase/"
    )

    assert response.status_code == 400

    assert response.data["detail"] == "Vehicle is out of stock."

@pytest.mark.django_db
def test_purchase_invalid_vehicle(user_client):

    response = user_client.post(
        "/api/vehicles/999/purchase/"
    )

    assert response.status_code == 404