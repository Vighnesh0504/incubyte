import pytest

from vehicles.models import Vehicle


@pytest.mark.django_db
def test_admin_can_restock_vehicle(admin_client):

    vehicle = Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=2,
    )

    response = admin_client.post(
        f"/api/vehicles/{vehicle.id}/restock/",
        {
            "quantity": 10
        },
        format="json",
    )

    assert response.status_code == 200

    vehicle.refresh_from_db()

    assert vehicle.quantity == 12

@pytest.mark.django_db
def test_normal_user_cannot_restock(user_client):

    vehicle = Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=2,
    )

    response = user_client.post(
        f"/api/vehicles/{vehicle.id}/restock/",
        {
            "quantity": 10
        },
        format="json",
    )

    assert response.status_code == 403