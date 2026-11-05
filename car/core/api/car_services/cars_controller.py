from car.core.config import BASE_URL
class CarController:
    def __init__(self,session, base_url=BASE_URL):
        self.session = session
        self.base_url = base_url

    def get_cars(self, params = None):
        response = self.session.get(f"{self.base_url}/cars", params=params)
        return response

