from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3b"
points = 1

@test_case()
def test_mean(env):
    p2 = env["Question3b"].p2
    p3 = env["Question3b"].p3
    p4 = env["Question3b"].p4
    
    assert_equal((p2 - p3), 0)
    assert_equal((p2*p3)+p4, 0)