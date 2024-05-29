# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2"
points = 1
@test_case()
def test_q2(env):

    be = env["Question2"].cv.best_estimator_ 
    true_be = 5
    assert_equal(true_be, be.max_depth)
    


