from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3a"
points = 1

@test_case()
def test_mean(env):
    n_samples = env["Question3a"].n_samples
    y = env["Question3a"].y

    assert_equal(len(y), n_samples)
    assert_almost_equal(y.mean(), 2.963 , places=2)
    assert_almost_equal(y.mean(), 2.963 , places=2)
