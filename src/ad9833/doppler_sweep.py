import AD9833
import utime as time

print("Setting up AD9833")
ad9833 = AD9833.AD9833(sdo=3, clk=2, cs=1,  fmclk = 25)

while True:
    center_frequency = 1_000_000
    ad9833.set_frequency(fout=center_frequency, freqSelect=0)
    ad9833.set_phase(pout=0, phaseSelect=0, rads=False)
    ad9833.set_mode('SIN')
    ad9833.select_freq_phase(FS=0, PS=0)
    print("beginning sweep")
    for doppler_offset in range(200_000, -200_000, -1):
        if doppler_offset % 10000 == 0:
            print("Setting offset to " + str(doppler_offset))
        ad9833.set_frequency(fout=center_frequency + doppler_offset, freqSelect=0)
        #time.sleep_us(10)

# output off
print("Turning off")
ad9833.set_mode('OFF')

