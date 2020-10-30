# -*— coding:utf-8 —*—
# @time ：2020/10/2818:59
# @Auttor :wiwi
# @File :test_calc.py
# 调用函数
import allure
import pytest

from test_pytest.core.calc import Calc
# 定义一个测试的类

@allure.feature("一个测试的类")
class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        print("setup")

    @pytest.mark.parametrize('a, b, c', [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, 1],
        [5.5, 6.5, 36.3],
        [5535.5684, 253.5565,1403579.3490146],
        [5, 0, 0],
        [-5, 0, 0]
    ])
    @allure.story("正常值乘法用例")
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @pytest.mark.parametrize(('a,b'),
        ['a',3],
        [4,'t']
        [4, ',']

    )
    @allure.story("异常值乘法用例")
    def test_mul(self, a, b):
        # assert self.calc.mul(a, b) == c
        with pytest.raises(Exception):
            assert self.calc.div(a, b)
    # 正常值例子
    @pytest.mark.parametrize('a, b, c', [
        [2, 2, 1],
        [0.2, 0.1, 2],
        [10, 3, 3.3333333333333335],
        [0, 6, 0],
        [0, -6, 0],
        [-0.2, -0.1, 2],
        [0.2, -0.1, -2],
        [-0.2, 0.1, -2]
    ])
    @allure.story("正常值除法用例")
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @pytest.mark.parametrize('a, b', [
        [2, 0],
        [0.2, 0],
        [0, 0],
        ['a', 0],
        [0.2, 'b'],
        ['.', 5],
        [0.2, '*'],
        [0.2, '-']
    ])
    @allure.story("异常值除法用例")
    def test_div2(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    def teardown_class(self):
        pass
    # # 流程示例
    # def test_process(self):
    #     r1=self.calc.mul(1, 2)
    #     r2=self.calc.div(2, 1)
    #     assert r1 == 2
    #     assert r2 == 2