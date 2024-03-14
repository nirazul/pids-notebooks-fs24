from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 4b"
points = 1
@test_case()
def test_hist_major(env):
  hist_major = env["Question4b"].hist_major
  ylim5 = hist_major.get_ylim()
  assert_equal(ylim5 ,(0.0, 131250.0))