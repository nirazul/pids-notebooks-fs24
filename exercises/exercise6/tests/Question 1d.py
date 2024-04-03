from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1d"
points = 2

@test_case()
def test_mean_median(env):
    mean_x = env["Question1d"].mean_x
    median_x = env["Question1d"].median_x
    std_x = env["Question1d"].std_x
    

    assert_almost_equal((mean_x - std_x)/median_x, 0.771 , places=2)
    assert_almost_equal((mean_x ** std_x)+ median_x, 186.349 , places=2)
    