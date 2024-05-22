from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 4c"
points = 1


@test_case()
def test_subplots(env):
    p_value = env["Question4c"].p_value
    lb = 0.02
    ub = 0.25
    assert_true(lb < p_value < ub)
