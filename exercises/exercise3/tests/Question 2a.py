from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2a"
points = 1
@test_case()
def test_unemployed_plot(env):
  plot_unemployed_rank = env["Question2a"].plot_unemployed_rank
  xlim = plot_unemployed_rank.get_xlim()
  ylim = plot_unemployed_rank.get_ylim()
  test = 160 < xlim[1] < 190
  assert(test == True)
  test2 = 0.1 < ylim[1] < 0.3
  assert(test2 == True)


