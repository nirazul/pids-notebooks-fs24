from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1e"
points = 1
@test_case()
def test_color_code_plot(env):
  color_code_plot = env["Question1e"].color_code_plot
  asia_bins = env["Question1e"].asia_bins
  
  assert(10 < color_code_plot.get_ylim()[1] < 11)
  assert(3 <= asia_bins <= 5)

