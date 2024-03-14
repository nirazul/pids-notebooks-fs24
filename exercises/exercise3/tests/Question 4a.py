from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 4a"
points = 1
@test_case()
def test_top_10(env):
  top_10 = env["Question4a"].top_10
  assert(top_10.shape == (10, 21))
  assert(top_10["Median"][0] == 110000)
