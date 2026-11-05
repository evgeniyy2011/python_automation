from car.functional.tests.conftest import car_session
import pytest
from car.core.api.car_services.cars_controller import CarController
import logging

logger = logging.getLogger(__name__)

class TestCars:

    @pytest.mark.parametrize("sort_by, limit",[
                             ("price", 5),
                             ("year", 10),
                             ("brand", 7),
                             ("engine_volume", 8),
                             ("price", 15),
                             ("year", 20),])

    def test_search_cars(self, car_session,sort_by, limit):

        params = {"sort_by" : sort_by,
                  "limit" : limit
        }
        logger.info(f"Search cars sort_by:{sort_by}, limit:{limit}")

        car_controller = CarController(car_session)
        response = car_controller.get_cars(params=params)
        assert response.status_code == 200, "Status code is not 200"

        cars = response.json()
        value =[i[sort_by] for i in cars]

        assert len(cars) == limit
        assert value == sorted(value)
