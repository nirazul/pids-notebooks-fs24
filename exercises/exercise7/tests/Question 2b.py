
from otter.test_files import test_case
from asserts import *
import numpy as np

OK_FORMAT = False
name = "Question 2b"
points = 2
@test_case()
def test_mean_est(env):
  mean_est = env["Question2b"].mean_est
  P = env["Question2b"].P
  assert_equal(mean_est.shape, (P,))
  assert_true(np.max(mean_est[0:100]) > 5.1)
  assert_true(np.all(np.abs(mean_est[1000:] - 5) < 2e-1))
  