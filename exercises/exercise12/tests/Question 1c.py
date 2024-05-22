from asserts import *
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 1c"
points = 1


@test_case()
def test_solution(env):  
    q2 = env["Question1c"]
    assert_equal(q2.cold_temperatures.shape, (10,3))
    assert_equal(q2.cold_temperatures["Temperature"].max(), 12)
    assert_equal(q2.cold_temperatures["Temperature"].min(), 3)

