from Home_work_12.features import plus
import pytest

class Test_Additions_valid_data:

    @pytest.mark.parametrize('number_a, number_b, expected_result', [(5,5,10), (10,10,20), (100,105,205)])
    def test_addition(self, number_a, number_b, expected_result):

        actual_result = plus(number_a,number_b)

        assert  actual_result == expected_result, (f"{number_a} + {number_b} shuld be = {expected_result}")


class Test_Additions_invalid_data:

    @pytest.mark.parametrize("number_a, number_b, expected_result",[(20,27,80),(11,68,88),(10,0,50)])
    def tests_addition(self, number_a, number_b, expected_result):
        actual_result = plus(number_a, number_b)

        assert expected_result == actual_result,(f"AHTUNG AHTUNG{number_a} + {number_b} shuld be = {expected_result}")