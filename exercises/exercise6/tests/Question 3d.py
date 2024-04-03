from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3d"
points = 1

@test_case()
def test_mean(env):
    mean_y = env["Question3d"].mean_y
    std_y = env["Question3d"].std_y
    median_y = env["Question3d"].median_y
    
    assert_almost_equal((mean_y - std_y)/median_y, 0.335 , places=2)
    assert_almost_equal((mean_y ** std_y)+ median_y, 11.491 , places=2)