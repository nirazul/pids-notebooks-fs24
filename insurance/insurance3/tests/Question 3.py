from asserts import *
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_solution(env):  
    ax = env["Question3"].plot
    xlim = ax.get_xlim()
    assert(-1 < xlim[0] < 1)
    assert(300 < xlim[1] < 350)

