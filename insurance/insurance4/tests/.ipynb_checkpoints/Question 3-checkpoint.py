from asserts import *
from otter.test_files import test_case

OK_FORMAT = False
name = "Question 3"
points = 1


@test_case()
def test_solution(env):  
    mpg_us8 = env["Question3"].mpg_us8
    assert(mpg_us8.shape == (103, 9))
    
    xlabel = env["Question3"].plot.axes[0][0].get_xlabel()
    ylabel = env["Question3"].plot.axes[0][0].get_ylabel()
    assert(xlabel == "mpg" and ylabel == "horsepower")

