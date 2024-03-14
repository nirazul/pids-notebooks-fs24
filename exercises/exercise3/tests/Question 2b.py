from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2b"
points = 1
@test_case()
def test_unemployed_plot(env):
  plot_salary_rank = env['Question2b'].plot_salary_rank
  xlim2 = plot_salary_rank.get_xlim()
  ylim2 = plot_salary_rank.get_ylim()
  test = 170 < xlim2[1] < 185
  assert(test == True)
  test2 = 120000.0 < ylim2[1] < 150325.0
  assert_equal(test2, True)