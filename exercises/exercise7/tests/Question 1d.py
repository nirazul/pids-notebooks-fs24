
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1d"
points = 2
@test_case()
def test_gaussian_plot(env):
  gaussian_plot = env["Question1d"].gaussian_plot
  assert_true(0 <= gaussian_plot[0].axes.get_ylim()[1] <= 1)
