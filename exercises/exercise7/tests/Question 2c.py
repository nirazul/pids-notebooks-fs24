
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2c"
points = 2
@test_case()
def test_mean_abs_err(env):
  abs_err = env["Question2c"].abs_err
  assert_true(abs_err[-1] < 0.03)
  assert_true(np.abs(abs_err[-1] - abs_err[-2]) < 1e-2)
  