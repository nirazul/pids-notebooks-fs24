from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1b"
points = 4
@test_case()
def test_q1b(env):
    k = env["Question1b"].k
    means = env["Question1b"].means
    assert_equal(len(means), k)
    assert_almost_equal(means.mean(), 9.992 , places=2)
    assert_almost_equal(means.std() , 0.677 , places=2)
