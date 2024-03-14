from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2c"
points = 1
@test_case()
def test_lowwage_rank(env):
  plot_lowwage_rank = env['Question2c'].plot_lowwage_rank
  xlim3 = plot_lowwage_rank.get_xlim()
  test = -25 < xlim3[0] < 2
  assert_equal(test, True)