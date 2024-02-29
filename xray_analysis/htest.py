# htest.py
import numpy as np
from scipy.optimize import minimize
from scipy.stats import chi2

def calculate_z_n_squared(phases, n):
    """Calculate the Z_n^2 statistic for a given harmonic n."""
    return 2 * sum(np.cos(2 * np.pi * n * phases))**2 + 2 * sum(np.sin(2 * np.pi * n * phases))**2

def h_test(phases, max_harmonics=20):
    """Perform the H-test for a given set of phases.
    
    Args:
        phases (array-like): The phases of the events, assumed to be between 0 and 1.
        max_harmonics (int): The maximum number of harmonics to consider.

    Returns:
        tuple: The maximum H statistic and the optimal number of harmonics.
    """
    H_max = 0
    optimal_harmonic = 0
    for n in range(1, max_harmonics + 1):
        Z_n_squared = calculate_z_n_squared(phases, n)
        H = Z_n_squared - 4 * n + 4
        if H > H_max:
            H_max = H
            optimal_harmonic = n

    # Calculate the significance of the H_max value.
    # The significance (p-value) is the probability of observing a value of H_max or higher
    # from the chi-squared distribution with 2 * optimal_harmonic degrees of freedom.
    p_value = 1 - chi2.cdf(H_max, 2 * optimal_harmonic)
    
    return H_max, optimal_harmonic, p_value

def optimize_period(phases, period_guess, time, flux):
    """Optimize the period using the H-test as an objective function.
    
    Args:
        phases (array-like): Initial phases computed from an initial period guess.
        period_guess (float): Initial guess for the period.
        time (array-like): Time observations of the light curve.
        flux (array-like): Corresponding flux values of the light curve.
    
    Returns:
        float: Optimized period.
    """
    def objective(period):
        phases = (time % period) / period
        H_max, _, _ = h_test(phases)
        return -H_max  # Minimize the negative H to find the maximum

    result = minimize(objective, period_guess, method='L-BFGS-B', bounds=[(0.5 * period_guess, 1.5 * period_guess)])
    return result.x[0]
