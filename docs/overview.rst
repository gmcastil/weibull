Overview
========

Planning
--------
Thoughts on the UI:

- Really just an interface to a system that generates a pair of arrays of LET
  and cross sections when created with the appropriate input data

Thoughts on the data structure:

- Weibull parameters need to be exposed but also changed and the data
  structure updated
- Created with a table of cross section and LET values

So, probably something like a ``CrossSection`` class with the following public
attributes:

  CrossSection.__init__(max, min)
  - Sets max and min LET to consider - defaults to 0 and 100
  - Complains if either is negative or max is not greater than min
  - These are not expected to change

  CrossSection.fit(LET, cross_section)
  - Accepts a table of LET and cross section data (discrete points)
  - Returns cross section as a function of LET between max and min.
  - Returns chi-squared statistic for the fit relative to the data
  - Returns Weibull parameters

  CrossSection.update(parameters)
  - Complains if update() has been run without initially running fit()
  - Accepts a dictionary, containing Weibull parameters and computes the
    Weibull function for those parameters
  - Returns cross section as a function of LET between 0 and 100 (again,
    something that can be changed)
  - Returns chi-squared statistic for the function and the data
  - Perhaps two update methods - one for cross section and LET values being
    altered and another for Weibull parameters being updated

Use Cases
---------
User creates some values in a table (either manually or by Excel or something).
User asks for an initial fit and expects the following:
- UI performs an initial plot of the data
- Weibull parameters are populated in the UI
- Chi-squared statistic gets calculated in the UI

After the initial fit, the user changes data points:
- UI performs a new plot of the data
- New Weibull parameters are populated in the UI
- New chi-squared statistic gets calculated and shown in the UI

Changing any value in the table should trigger an immediate
update of the Weibull parameters, chi-squared statistic and the plot.  Changing
any of the Weibull parameters should also trigger an immediate update of the
chi-squared statistic and the plot.


  



Interface
---------
Fundamentally provided functionality is to allow interactive fitting an SEE
cross section to a set of observables.  The general use case is to allow users
to enter cross section vs. LET measurements or observables and fluence vs. LET
measurements.  Once data are available, a preliminary Weibull fit can be
performed and displayed to the user, along with initial estimates for the
parameters.  These values can then be tweaked and the cross section updated and
redisplayed to the user.

Some initial interface requirements:

- Table to view cross section and LET values
- Once data are loaded, perform a best fit and display the chi-squared
  statistic and display the datapoints and Weibull fit to the data
- Support manual entry of cross section data or import from .xlsx or .csv files
- Display Weibull parameters to the user, probably in spinboxes
- Any change in Weibull parameters or data points by the user shall update the
  current curve fit, chi-squared statistic, and display

Things users can do:

- Import data from spreadsheet
- Manually enter data in the input table
- Clear data table
- Any change to the data table or Weibull parameters updates the chi-squared
  value and cross section vs. LET values.
