from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1b"
points = 1
@test_case()
def test_mean_obesity(env):
    mean_obesity_level = env["Question1b"].mean_obesity_level
    assert_almost_equal(mean_obesity_level, 0.21925)

