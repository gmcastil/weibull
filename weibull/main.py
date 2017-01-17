
"""
User interface should support the following workflow:

- Open a blank table with no Weibull parameters shown
- Type in or copy tables from Excel
- Select heavy ion or proton cross section
- When created, get parameter dictionary for the fit
  - Populate Weibull parameters (fit)
  - Calculate chi-squared (chi-squared)
  - Get a plottable cross section (values)
  - Display plottable cross section (UI)
- After created, changing data does the following
  - Repopulate Weibull parameters from altered data (fit)
  - Calculate chi-squared (chi-squared)
  - Get a plottable cross section (values)
  - Display plottable cross section (UI)
- After created, changing Weibull paramters does the following
  - Obbtains chi-squared value for non-best fit (chi-squared)
  - Get a plottable cross section (values)
  - Display plottable cross section (UI)
  - Notifies user in UI that Weibull fit is non-best fit (UI)

Need the following functions:

- Calculate LET or energy versus cross section given Weibull parameters
- Calculate Weibull paramters from measured datapoints
- Calculate chi squared from measured datapoints and Weibull parameters

"""
