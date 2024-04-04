# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2"
points = 1
@test_case()
def test_subplots(env):
    xlim = env["Question2"].plot.axes[0][0].get_xlim()
    ylim = env["Question2"].plot.axes[0][0].get_ylim()
    assert(80 <= ylim[1] <= 82 or 125 <= ylim[1] <= 127)
