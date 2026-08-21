from Home_work_10.Home_work_10_2 import Triangle
import pytest

class TestTriangle:

    @pytest.mark.parametrize("side_a, side_b, side_c, expected_result",[(10, 10, 15, 35), (20, 10, 30, 60)])
    def test_triangle_perimetr(self, side_a: int, side_b: int, side_c: int, expected_result: int):
        tr_p = Triangle(tr_a=side_a, tr_b=side_b, tr_c=side_c)
        result = tr_p.perimetr()

        assert result == expected_result

    @pytest.mark.parametrize("side_a, side_h, expected_result",[(10,20,100),(30,20,300)])
    def test_triangle_square(self, side_a:int, side_h:int, expected_result:int):
        tr_s = Triangle(tr_a=side_a, tr_h=side_h)
        result = tr_s.square()

        assert  result == expected_result
