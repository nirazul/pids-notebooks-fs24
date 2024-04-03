from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2a"
points = 2

@test_case()
def test_mean(env):
    x1 = env["Question2a"].x1
    x2 = env["Question2a"].x2
    x12 = env["Question2a"].x12
    
    assert_almost_equal((x1.mean() + x2.mean())/x12.mean(), 2.000 , places=2)
    assert_almost_equal((x1.mean() - x2.mean())*x12.mean(), -120.670 , places=2)
