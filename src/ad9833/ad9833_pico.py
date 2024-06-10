# Started from
# https://github.com/owainm713/AD9833-MicroPython-Module/blob/main/AD9833example.py
import AD9833
import utime as time

print("Setting up AD9833")
ad9833 = AD9833.AD9833(sdo = 3, clk = 2, cs = 1,  fmclk = 25)

# setup frequency and phase registers
ad9833.set_frequency(1300,0)
ad9833.set_frequency(2600, 1)
ad9833.set_phase(0, 0, rads = False)
ad9833.set_phase(180, 1, rads = False)

delay = 1.5  # number of seconds to display each feature
print("Initial sleep")
time.sleep(delay)

# freq 0 Sin wave output
ad9833.select_freq_phase(0,0)
ad9833.set_mode('SIN')
print("Sine wave output, F0")
time.sleep(delay)

# freq 1 Sin wave output
ad9833.select_freq_phase(1,0)
print("Sine wave output, F1")
time.sleep(delay)

# freq 0 Triangle wave output
ad9833.select_freq_phase(0,0)
ad9833.set_mode('TRIANGLE')
print("Triangle output, F0")
time.sleep(delay)

# freq 0 Square wave output
ad9833.set_mode('SQUARE')
print("Square wave output, F0")
time.sleep(delay)

# freq 0 divide by 2 Square wave output
ad9833.set_mode('SQUARE/2')
print("Square/2 output, F0")
time.sleep(delay)

# freq 0 Sin wave output
ad9833.set_mode('SIN')
print("Sine wave, F0")
time.sleep(delay)

# change freq 0 to 1700 Hz, Sin wave output
ad9833.set_frequency(1700,0)
print("Sine wave, 1700 Hz")
time.sleep(delay)

# output off
print("Turning off")
ad9833.set_mode('OFF')
