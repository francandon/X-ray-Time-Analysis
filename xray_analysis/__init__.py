from .io import read_fits_light_curve
from .analysis import get_pulse_profile, optimize_light_curve_period
from .htest import h_test

def analyze_light_curve(filename, period_guess):
    time, flux = read_fits_light_curve(filename)
    
    # Optimize the period based on the initial guess and the light curve data
    optimized_period = optimize_light_curve_period(time, flux, period_guess)
    
    # Now, with the optimized period, proceed to get the pulse profile or further analysis
    phase, profile = get_pulse_profile(time, flux, optimized_period)
    
    # Perform the H-test using the optimized period to find the H statistic and significance
    H_max, optimal_harmonic, p_value = h_test(phase)
    
    return optimized_period, H_max, optimal_harmonic, p_value
