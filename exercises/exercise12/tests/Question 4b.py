# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 4b"
points = 1
@test_case()
def test_q2(env):

    mean_est = env["Question4b"].mean_fraction_foreigners
    std_est = env["Question4b"].stddev_fraction_foreigners
    melb = 0.35
    meub = 0.36
    stdup = 0.11
    
    assert_true(melb < mean_est <meub)
    assert_true(0 < std_est < stdup)
# -


