from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_subplots(env):
    p_value = env["Question3"].p_value
    lb = 0.02
    ub = 0.25
    assert_true(lb < p_value < ub)
