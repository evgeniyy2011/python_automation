import requests
from requests.auth import HTTPBasicAuth
import pytest
import logging
from car.core.config import BASE_URL, USER_NAME, USER_PASWORD

logger = logging.getLogger(__name__)

@pytest.fixture(scope="class")
def car_session():

    logger.info("Autorization started")
    session = requests.Session()
    response = session.post(f"{BASE_URL}/auth", auth=HTTPBasicAuth(USER_NAME, USER_PASWORD))


    # print(response.status_code)
    assert response.status_code == 200, "Status code is not 200"
    token = response.json()['access_token']
    # print(token)

    session.headers.update({"Authorization": f"Bearer {token}"})
    logger.info("Autorization Succssesful")
    return session