"""Main test class for weibull fitter"""
import csv

import weibull

DATA = "./data.csv"

class TestWeibullBase(object):
    """Base class for testing Weibull module"""

    def setup_method(self):
        pass

    def teardown_method(self):
        pass

class TestWeibullCalculations(TestWeibullBase):
    """Test Weibull function calculations"""

def xs_from_file(data):
    """Returns a calculated cross section from Weibull parameters"""

    with open(data) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',', quotechar='#')
