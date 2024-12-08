from rtlsdr import RtlSdr
from rtlsdr import *

sdr = RtlSdr()

# configure device
sdr.sample_rate = 1600000  # Hz
sdr.center_freq = 868950000 # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

print(sdr.read_samples(512))
#print(sdr.packed_bytes_to_iq(sdr.read_samples(512)))


