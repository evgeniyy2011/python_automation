import logging

import pytest
import requests
from requests.auth import HTTPBasicAuth


BASE_URL = "http://127.0.0.1:8080"

logger = logging.getLogger(__name__)


@pytest.fixture(scope="class")
def car_session():

    session = requests.Session()

    logger.info("Authorization started")

    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )

    assert response.status_code == 200, (
        f"Authorization returned {response.status_code}, expected 200"
    )

    access_token = response.json()["access_token"]

    session.headers.update({
        "Authorization": "Bearer " + access_token
    })

    logger.info("Authorization successful")

    return session


class TestCars:

    @pytest.mark.parametrize(
        "sort_by, limit",
        [
            ("price", 5),
            ("price", 10),
            ("year", 5),
            ("year", 15),
            ("engine_volume", 10),
            ("brand", 7),
        ]
    )
    def test_search_cars(self, car_session, sort_by, limit):

        params = {
            "sort_by": sort_by,
            "limit": limit
        }

        logger.info(
            f"Searching cars: sort_by={sort_by}, limit={limit}"
        )

        response = car_session.get(
            f"{BASE_URL}/cars",
            params=params
        )

        assert response.status_code == 200, (
            f"Cars request returned {response.status_code}, expected 200"
        )

        cars = response.json()

        assert len(cars) == limit, (
            f"Expected {limit} cars, but received {len(cars)}"
        )

        values = [car[sort_by] for car in cars]

        assert values == sorted(values), (
            f"Cars are not sorted correctly by {sort_by}"
        )

        logger.info(
            f"Test passed: sort_by={sort_by}, limit={limit}"
        )