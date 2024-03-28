from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2c"
points = 3
@test_case()
def test_stroke_hypertension(env):
    probability_stroke_hypertension = env["Question2c"].probability_stroke_hypertension
    assert_is_instance(probability_stroke_hypertension, float)
    assert_almost_equal(probability_stroke_hypertension, 0.13 , places=2)
## test ##


