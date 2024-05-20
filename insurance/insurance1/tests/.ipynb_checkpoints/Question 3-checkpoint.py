from asserts import *
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_solution(env):  
    q3 = env["Question3"]
    assert_equal(q3.pew_catholic.shape, (6, 3)) 

