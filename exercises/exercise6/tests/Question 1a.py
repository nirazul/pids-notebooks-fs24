from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1a"
points = 1

@test_case()
def test_samples(env):
  n_samples = env["Question1a"].n_samples
  x = env["Question1a"].x
  assert_equal(len(x), n_samples)
  assert_almost_equal(x.mean(), 9.968 , places=2)
  assert_almost_equal(x.std() , 2.249 , places=2)
