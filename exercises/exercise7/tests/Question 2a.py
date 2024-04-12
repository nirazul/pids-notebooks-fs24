
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2a"
points = 1
@test_case()
def test_poisson_plot(env):
  poisson_plot = env["Question2a"].poisson_plot
  assert_true(0.16 <= poisson_plot[0].axes.get_ylim()[1] <= 0.19)