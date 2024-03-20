from otter.test_files import test_case
from asserts import *

OK_FORMAT = False
name = "Question 1d"
points = 2
@test_case()
def test_unemployed_plot(env):
    cities = env["Question1d"].cities_with_continents    
    assert_almost_equal(cities.loc[(cities["City"] == "Vienna")]["Sunshine hours(City)"].values[0], 1884.0)
    assert_almost_equal(cities.loc[(cities["City"] == "Stockholm")]["Cost of a bottle of water(City)"].values[0], 1.72)
    assert_almost_equal(cities.loc[(cities["City"] == "Milan")]["Obesity levels(Country)"].values[0], 0.199)
    assert_almost_equal(cities.loc[(cities["City"] == "New York")]["Cost of a monthly gym membership(City)"].values[0], 64.66)