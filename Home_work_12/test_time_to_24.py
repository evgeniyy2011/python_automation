import pytest
from assertpy import soft_assertions

from Home_work_12 import features

class Test_time_format:

    @pytest.mark.parametrize("time, expected_res",[("5:15 pm", "17:15")])
    def test_converter_time(self, time:str, expected_res:str):
        new_time = features.convert_to_24_hour(time_str=time)

        assert new_time == expected_res, f"Time should be in format hh:mm am/pm"



    @pytest.mark.parametrize("time, expected",[("10:29 am", "10:29"),("11:20 pm", "10:10")])
    def test_converter_time_ver2(self, time:str, expected:str):

        with soft_assertions():
            assert features.convert_to_24_hour(time_str=time) == expected

