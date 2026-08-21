from Home_work_10.Home_work_10_2 import Cube
import pytest



class Test_cube:

    @pytest.mark.parametrize("parametr_a, expected_result",[(4, 48), (10, 120)])
    def test_perimetr_cub(self, parametr_a: int, expected_result: int):
        cub_p = Cube(cb_a=parametr_a)
        result = cub_p.perimetr()

        assert result == expected_result, (f"Cub's perimetr of {parametr_a} equal {expected_result}")



    @pytest.mark.parametrize("parametr_a, expected_result",[(4,96),(10,600)])
    def test_squere_square(self,parametr_a:int, expected_result:int):
        cub_s = Cube(cb_a=parametr_a)
        result = cub_s.square()

        assert result == expected_result, (f"Cub's square of {parametr_a} equal {expected_result}")

