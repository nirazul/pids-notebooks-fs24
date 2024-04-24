from otter.test_files import test_case
from asserts import *
import numpy as np
import pandas as pd

OK_FORMAT = False
name = "Question 1b"
points = 3
@test_case()
def test_q1a(env):
    neighborhoods = env["Question1b"].neighborhoods
    
    assert_is_instance(neighborhoods, pd.DataFrame)
    assert_equal(neighborhoods[neighborhoods["wohnviertel_name"] == "Bachletten"]["increase_green_space"].iloc[0], 1)
    assert_equal(neighborhoods[neighborhoods["wohnviertel_name"] == "St. Johann"]["increase_green_space"].iloc[0], 1)
    assert_equal(neighborhoods[neighborhoods["wohnviertel_name"].str.startswith("Matth")]["increase_green_space"].iloc[0], 0)
   