
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1b"
points = 1
@test_case()
def test_samples(env):
    toss_sum = env["Question1b"].toss_sum
    M = env["Question1b"].M
    assert_equal(toss_sum.shape[0], M)
