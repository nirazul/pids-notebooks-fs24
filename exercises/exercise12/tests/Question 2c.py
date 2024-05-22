# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 2c"
points = 1
@test_case()
def test_subplots(env):
    ts1 = 0.0521
    ts2 = 0.9015
    
    p_xe3 = env["Question2c"].p_xe3
    p_xlt10 = env["Question2c"].p_xlt10
    assert(ts1 - 0.01 < p_xe3 < ts1 + 0.01 )
    assert(ts2 - 0.01 < p_xlt10 < ts2 + 0.01 )
# -


