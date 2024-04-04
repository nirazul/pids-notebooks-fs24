# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1"
points = 1
@test_case()
def test_subplots(env):
    mpg = env["mpg"]
    mpg_with_full_model_year = env["Question1"].mpg_with_full_model_year
    assert(mpg_with_full_model_year.shape ==  mpg.shape)
    assert(mpg_with_full_model_year["model_year"].min() == mpg["model_year"].min() + 1900)
    assert(mpg_with_full_model_year["model_year"].max() == mpg["model_year"].max() + 1900)
    
