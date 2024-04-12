
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1a"
points = 2
@test_case()
def test_samples(N, env):
    toss_coin_all = env["Question1a"].toss_coin_all
    M = env["Question1a"].M
    assert_equal(toss_coin_all.shape, (M, N))
    assert_true(np.abs(toss_coin_all.mean() - 0.5) < 0.05)



