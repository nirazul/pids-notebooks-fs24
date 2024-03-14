from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2e"
points = 1
@test_case()
def test_percentage(env):

  percentage = env["Question2e"].percentage 
  percentage_plot = env["Question2e"].percentage_plot

  test = ((0.09 < percentage[0] < 0.099) or (0.09*100 < percentage[0] < 0.099*100))
  assert_equal(test, True)

  ylim = percentage_plot[0].axes.get_ylim()
  test2 = -0.1 < ylim[0] < 0.1 and 0.37 < ylim[1] < 0.40
  assert_equal(test2, True)
