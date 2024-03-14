from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3a"
points = 1
@test_case()
def test_hist_median(env):
  hist_median_column = env['Question3a'].hist_median_column
  
  ylim = hist_median_column.axes.get_ylim()
  test2 = -0.1 < ylim[0] < 0.1 and 64 < ylim[1] < 65
  assert_equal(test2, True)
