# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3b"
points = 1
@test_case()
def test_q2(env):

    me = env["Question3b"].mean_est
    ae = env["Question3b"].abs_err
    melb = 0.95
    meub = 1.05
    aelb = 0.05
    
    assert_true(melb < me <meub)
    assert_true(0 < ae < aelb)
# -


