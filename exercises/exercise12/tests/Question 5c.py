from asserts import *
from otter.test_files import test_case
import random

OK_FORMAT = False
name = "Question 5c"
points = 1


@test_case()
def test_subplots(env):
    mlp = env["Question5c"].mlp
    layer_sizes = mlp.hidden_layer_sizes
    act = mlp.activation
    assert_equal(10, layer_sizes[0])
    assert_equal(7, layer_sizes[1])
    assert_equal("tanh", act)