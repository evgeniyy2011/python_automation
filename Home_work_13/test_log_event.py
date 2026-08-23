import pytest
from Home_work_13 import lesson_13


class Test_log:

    @pytest.mark.parametrize("name, stat",[("Alex", "success"),("Vova", "expired"),("John", "failed")])
    def test_log_event(self, name:str, stat:str ):
        lesson_13.log_event(username=name, status=stat)
        expected_row = f"Login event - Username: {name}, Status: {stat}"
        with open("login_system.log") as q:
            last_row = q.readlines()[-1]
            assert expected_row in last_row




