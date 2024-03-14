from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 5"
points = 1
@test_case()
def test_scatterplot(env):
  scatterplot = env["Question5"].scatterplot
  assert_equal('Median', scatterplot.get_xlabel())
