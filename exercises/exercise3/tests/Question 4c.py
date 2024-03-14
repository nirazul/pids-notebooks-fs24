from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 4c"
points = 1

@test_case()
def test_hist_major_engineering(env):
  hist_major_engineering = env["Question4c"].hist_major_engineering
  ylim = hist_major_engineering.get_ylim()
  assert(5.0 <= ylim[1] <= 7.0)