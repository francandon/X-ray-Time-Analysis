# io.py
from pathlib import Path
from astropy.io import fits

# Define the base directory for your data files
DATA_DIR = Path(__file__).parent / 'data'

def read_fits_light_curve(filename):
    # Construct the full path to the file
    file_path = DATA_DIR / filename
    
    # Use the full path to open the FITS file
    with fits.open(file_path) as hdul:
        data = hdul[1].data  # Adjust according to your FITS file structure
        time = data['TIME']
        flux = data['FLUX']
    return time, flux