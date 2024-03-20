
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1c"
points = 1
@test_case()
def test_unemployed_plot(env):
    obesity_levels_hist = env["Question1c"].obesity_levels_hist
    distribution = env["Question1c"].distribution
    answer = env["Question1c"].answer

    assert_true(7.5 <= obesity_levels_hist.get_ylim()[1] <= 8.5)
    assert_equal(distribution, "Bimodal")
    assert_equal(answer, 'no')