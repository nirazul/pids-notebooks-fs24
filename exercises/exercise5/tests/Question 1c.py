from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1c"
points = 1
@test_case()
def test_lower_30(env):
    probability_lower_30 = env["Question1c"].probability_lower_30
    assert_is_instance(probability_lower_30, float)
    assert_equal(probability_lower_30, 1)
    