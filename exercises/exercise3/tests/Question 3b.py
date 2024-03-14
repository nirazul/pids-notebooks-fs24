from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 3b"
points = 1
@test_case()
def test_subplots(env):
  ax1 = env["Question3b"].ax1 
  ax2 = env["Question3b"].ax2

  ylim1 = ax1.get_ylim()
  assert(75 <= ylim1[1] <= 80)
  ylim2 = ax2.get_ylim()
  assert(35 <= ylim2[1] <= 40)
  assert(ax2.patches[0].get_facecolor() == (0.0, 0.0, 0.0, 1.0))  
