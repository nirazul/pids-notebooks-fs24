from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2b"
points = 4

@test_case()
def test_mean(env):
    mean_x12 = env["Question2b"].mean_x12
    median_x12 = env["Question2b"].median_x12
    mode1_x12 = env["Question2b"].mode1_x12
    mode2_x12 = env["Question2b"].mode2_x12 
    assert_almost_equal((mean_x12 - median_x12)/mode1_x12, 0.000 , places=2)
    assert_almost_equal((mode1_x12 - mode2_x12)/ mean_x12, 1.198 , places=2)