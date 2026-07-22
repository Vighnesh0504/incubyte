import pytest

from vehicles.models import Vehicle


@pytest.mark.django_db
def test_search_by_make(user_client):

    Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )

    Vehicle.objects.create(
        make="BMW",
        model="X5",
        category="SUV",
        price=70000,
        quantity=3,
    )

    response = user_client.get(
        "/api/vehicles/search/?make=Toyota"
    )

    assert response.status_code == 200

    assert response.data["count"] == 1

    assert response.data["results"][0]["make"] == "Toyota"

@pytest.mark.django_db
def test_search_by_category(user_client):

    Vehicle.objects.create(
        make="Toyota",
        model="Fortuner",
        category="SUV",
        price=45000,
        quantity=4,
    )

    Vehicle.objects.create(
        make="Honda",
        model="City",
        category="Sedan",
        price=18000,
        quantity=7,
    )

    response = user_client.get(
        "/api/vehicles/search/?category=SUV"
    )

    assert response.status_code == 200

    assert response.data["count"] == 1

@pytest.mark.django_db
def test_search_by_price_range(user_client):

    Vehicle.objects.create(
        make="BMW",
        model="X5",
        category="SUV",
        price=70000,
        quantity=3,
    )

    Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )

    Vehicle.objects.create(
        make="Honda",
        model="City",
        category="Sedan",
        price=18000,
        quantity=2,
    )

    response = user_client.get(
        "/api/vehicles/search/?min_price=20000&max_price=30000"
    )

    assert response.status_code == 200

    assert response.data["count"] == 1

    assert response.data["results"][0]["model"] == "Corolla"

@pytest.mark.django_db
def test_search_is_case_insensitive(user_client):

    Vehicle.objects.create(
        make="Toyota",
        model="Corolla",
        category="Sedan",
        price=25000,
        quantity=5,
    )

    response = user_client.get(
        "/api/vehicles/search/?make=toy"
    )

    assert response.data["count"] == 1