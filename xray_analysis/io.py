# io.py
from astropy.io import fits

def read_fits_light_curve(filename):
    with fits.open(filename) as hdul:
        data = hdul[1].data  # Assuming the light curve data is in the first extension
        time = data['TIME']  # Adjust field names as necessary
        flux = data['FLUX']
    return time, flux