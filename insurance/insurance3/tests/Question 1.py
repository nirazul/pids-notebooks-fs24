# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_subplots(env):
  plot_q1 = env["Question1"].plot 
  xlim = plot_q1.get_xlim()
  ylim = plot_q1.get_ylim()
  assert(2 < xlim[1] < 3)
  assert(7 < ylim[1] < 8)

