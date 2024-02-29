# analysis.py
from .htest import optimize_period

def optimize_light_curve_period(time, flux, period_guess):
    """Optimize the period of the light curve using the H-test.

    Args:
        time (np.ndarray): Time data from the light curve.
        flux (np.ndarray): Flux data from the light curve.
        period_guess (float): Initial guess for the period.

    Returns:
        float: The optimized period.
    """
    optimized_period = optimize_period(time, flux, period_guess)
    return optimized_period
