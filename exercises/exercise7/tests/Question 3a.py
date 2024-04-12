
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 3a"
points = 2
@test_case()
def test_abserr(env):
  mean_abs_err = env["Question3a"].mean_abs_err
  err_plot = env["Question3a"].err_plot
  
  assert_true(mean_abs_err[-1] < 1e-1)
  assert_true(err_plot[0].axes.get_ylim()[0] >= 1e-2)
  assert_true(err_plot[0].axes.get_ylim()[1] <= 2e-1)
  