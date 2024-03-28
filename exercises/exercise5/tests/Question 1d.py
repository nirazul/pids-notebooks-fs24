from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1d"
points = 1
@test_case()
def test_probability_lower_6(env):
    probability_lower_6 = env["Question1d"].probability_lower_6
    assert_is_instance(probability_lower_6, float)
    assert_almost_equal(probability_lower_6, 0.41666666667, places=3)
## test ##


