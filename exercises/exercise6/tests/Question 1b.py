from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1b"
points = 1

@test_case()
def test_probabilities(env):
    p8 = env["Question1b"].p8
    p10 = env["Question1b"].p10
    p12 = env["Question1b"].p12

    assert_almost_equal((p8 - p12)/p10, 0)
    assert_almost_equal((p10*p12)+p8, 0.141 , places=2)
