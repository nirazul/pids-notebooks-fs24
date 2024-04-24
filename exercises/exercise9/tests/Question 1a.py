from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1a"
points = 1
@test_case()
def test_q1a(env):
    mean_2021 = env["Question1a"].mean_2021
    mean_2015 = env["Question1a"].mean_2015

    assert_almost_equal(mean_2021 - mean_2015, 0.0102, places=2)
    assert_almost_equal(mean_2015, 0.3199, places=2)
    assert_almost_equal(mean_2021, 0.3301, places=2)
