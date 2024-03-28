from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2b"
points = 1
@test_case()
def test_stroke_heart_disease(env):
    probability_stroke_heart_disease = env["Question2b"].probability_stroke_heart_disease
    assert_is_instance(probability_stroke_heart_disease, float)
    assert_almost_equal(probability_stroke_heart_disease, 0.170 , places=2)
## test ##

