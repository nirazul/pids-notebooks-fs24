from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 3c"
points = 1


@test_case()
def test_subplots(env):
    dp = env["Question3c"].density_plot
  
    assert_true(0.15 < dp[2][7].get_height() < 1)
