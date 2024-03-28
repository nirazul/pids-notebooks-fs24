from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2d - 1"
points = 2
@test_case()
def test_2d_1(stroke_df):
    assert_equal(stroke_df["high_glucose"].value_counts()[0], 4289)
## test ##


