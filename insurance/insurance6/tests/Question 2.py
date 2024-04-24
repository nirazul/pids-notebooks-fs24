# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2"
points = 1
@test_case()
def test_q2(env):

    me = env["Question2"].mean_est
    ae = env["Question2"].abs_err
    melb = 0.95
    meub = 1.05
    aelb = 0.05
    
    assert_true(melb < me <meub)
    assert_true(0 < ae < aelb)
# -


