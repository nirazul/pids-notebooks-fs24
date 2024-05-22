from asserts import *
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 1b"
points = 1

@test_case()
def test_solution(env):  
    q2 = env["Question1b"]
    assert_equal(q2.temperatures_sorted.shape, (15,3))
    assert_equal(q2.temperatures_sorted.iloc[0, 2], 20)
    assert_equal(q2.temperatures_sorted.iloc[14, 2], 3)


