
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 1c"
points = 1
@test_case()
def test_samples(env):
  density_plot = env["Question1c"].density_plot
  area_under_curve = np.sum(density_plot[0] * (density_plot[1][1] - density_plot[1][0]))
  assert_almost_equal(area_under_curve, 1, places=1)
