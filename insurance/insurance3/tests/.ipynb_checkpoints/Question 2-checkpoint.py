# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2"
points = 1
@test_case()
def test_subplots(env):
  ax1 = env["Question2"].axs[0] 
  ax2 = env["Question2"].axs[1]

  ylim1 = ax1.get_ylim()
  assert(20 <= ylim1[1] <= 25)
  ylim2 = ax2.get_ylim()
  assert(30 <= ylim2[1] <= 40)
  assert(ax2.patches[0] != None)  
