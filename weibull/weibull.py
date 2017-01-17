from collections import namedtuple
import numpy as np

MAX_LET = 100
MIN_LET = 0
MAX_ENERGY = 250
MIN_ENERGY = 0
SAMPLE_SIZE = 1000

HeavyIonXs = namedtuple('HeavyIonXs', ['LET', 'cross_section'], verbose=False)
ProtonXs = namedtuple('ProtonXs', ['energy', 'cross_section'], verbose=False)
WeibullParams = namedtuple('WeibullParams',
                           ['onset', 'shape', 'width', 'saturation',
                            'heavy_ion'], verbose=False)

def fit(data):
    """Calculates Weibull params given measured cross sections

    Args:
      data (tuple) - LET or energy, measured cross section, and ion type

    Returns:
      tuple - Wiebull params

    The return value of the fit() function is intended to be provided to the
    values() function to generate plottable cross sections

    """

def values(params):
    """Returns LET or energy versus cross section for a given Weibull fit

    Args:
      params (tuple): Weibull params
      step_size (float): Distance between energy or LET

    Returns:
      tuple - Heavy ion or proton cross sections suitable for plotting

    """
    if params.heavy_ion:
        LET = np.linspace(params.onset, MAX_LET, SAMPLE_SIZE)
        cross_section = _calc_Weibull(LET, params)
        return HeavyIonXs(LET, cross_section)
    else:
        energy = np.linspace(params.onset, MAX_ENERGY, SAMPLE_SIZE)
        cross_section = _calc_Weibull(energy, params)
        return ProtonXs(energy, cross_section)

def chi_squared(params, data):
    """Calculates the goodness of fit between measured and predicted datasets

    Args:
      data (ndarray) - LET or energy, measured cross section, and ion type
      params (tuple): Weibull parameters

    Returns:
      float - Pearson chi-squared test statistic

    """


def _calc_Weibull(data, params):
    """Calculates a Weibull function for a given LET or energy

    Args:
      data (ndarray): LET or energy range to calculate Weibull function for
      params (tuple): Weibull parameters

    Returns:
      ndarray - Calcuated cross section

    """
    exponent = (-1) * np.power(np.divide(data, params.width), params.shape)
    return params.saturation * (1 - np.exp(exponent))
