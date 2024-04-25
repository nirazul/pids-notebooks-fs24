from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_subplots(env):
    q3 = env["Question3"]
    ci = q3.ci
    
    lb = 0.6
    ub = 0.75
    assert_almost_equal(ci[0], lb, places = 1)
    assert_almost_equal(ci[1], ub, places = 1)
