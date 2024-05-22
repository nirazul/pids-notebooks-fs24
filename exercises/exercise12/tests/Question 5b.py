# +
from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 5b"
points = 1
@test_case()
def test_q2(env):

    regr = env["Question5b"].regr 
    X = env["Question5b"].X
    y_pred = regr.predict(X)    
    assert_equal((150, 3), X.shape)
    assert_equal(150, y_pred.shape[0])
    assert_almost_equal(1.2, y_pred.mean(), 1)
    


