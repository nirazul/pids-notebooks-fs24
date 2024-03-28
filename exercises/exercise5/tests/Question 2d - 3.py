from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2d - 3"
points = 1
@test_case()
def test_probability_high_glucose_strokee(env):
    probability_high_glucose_stroke =  env["Question2d3"].probability_high_glucose_stroke
    assert_is_instance(probability_high_glucose_stroke, float)
    assert_almost_equal(probability_high_glucose_stroke, 0.373, places = 2)
## test ##


