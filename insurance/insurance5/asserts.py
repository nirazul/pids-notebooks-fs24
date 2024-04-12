def assert_equal(expected, actual):
    assert expected == actual,  f"{actual} does not equal {expected}"
    
def assert_almost_equal(expected, actual, places = 2):
    assert abs(expected - actual) < float(f"1e-{places}"), f"{actual} does not equal {expected} for given precision 1e-{places}"

def assert_true(exp):
    assert(exp), f"{exp} is not true"

def assert_is_instance(value, tpe):
    assert (isinstance(value, tpe)), f"{value} is not instance of {tpe}"
