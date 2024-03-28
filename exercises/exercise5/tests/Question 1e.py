from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1e"
points = 2
@test_case()
def test_probability_higher_8(env):
    probability_higher_8 = env["Question1e"].probability_higher_8
    assert_is_instance(probability_higher_8, float)
    assert_almost_equal(probability_higher_8, 0.8333333333333334 , places=2)
## test ##



