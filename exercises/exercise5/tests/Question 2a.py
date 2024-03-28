from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2a"
points = 1
@test_case()
def test_probability_stroke(env):
    probability_stroke = env["Question2a"].probability_stroke
    assert_is_instance(probability_stroke, float)
    assert_almost_equal(probability_stroke, 0.04872 , places = 2)
## test ##
