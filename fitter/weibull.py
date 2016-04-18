def fit(x, y):
    """Computes parameters for a Weibull CDF from experimental values

    Args:
      x (float): Values for energy or LET of cross section
      y (float): Observed cross sections at each energy or LET

    Returns:
      dict - Parameters for a four parameter Weibull CDF

    The elements of the returned dictionary are the following:

      shape
      onset
      width
      saturation
      chi_square

    Assumes that the lowest energy or LET in `x` is the onset or
    threshold value and that the maximum value in `y` is the
    saturation cross section.  Practically speaking, one often assumes
    that onset has been established if there is at least two orders of
    magnitude between onset and saturation.

    """
    pass

def weib_func(energy, parameters):
    """Calculates the Weibull CDF at a given energy

    Args:
      energy (float): Value for energy or LET to compute for
      parameters (dict): Weibull parameters

    Returns:
      float - Value of the Weibull CDF at the energy provided

    """
    pass

