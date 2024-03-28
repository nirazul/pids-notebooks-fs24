from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2d - 2"
points = 1
@test_case()
def test_stroke_high_glucose(env):
    probability_stroke_high_glucose =  env["Question2d2"].probability_stroke_high_glucose
    assert_is_instance(probability_stroke_high_glucose, float)
    assert_almost_equal(probability_stroke_high_glucose, 0.113 , places = 2)
## test ##
