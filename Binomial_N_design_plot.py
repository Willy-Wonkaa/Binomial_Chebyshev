from Transfomer_design import *
import matplotlib.pyplot as plt
#I'm going to match 300 ohm load to 50 ohm load
Z0 = 50
ZL = 300
# central frequency f0 set at 2.5 GHz, light speed in vacuum, central wavelength (at f0), physical length of each section
f0 = 2.5e9
c = 3e8
lambda0 = c/f0
sect_length = lambda0/4
# frequency sweep parameters
fmin = 0
fmax = 5e9
nstep = 1000
# We will design 1-8 sections of binomial filter and see how bandwidth increases
Nmin = 1
Nmax = 8
Nstep = 1
i = Nmin
while i <= Nmax:
    #Design i section binomial transformer
    Zn = binom_design(i, Z0, ZL)
    print(Zn) 
    # Frequency swept to find reflection coefficients
    gammafreqsweep = refl_coeff_fsweep(Zn, f0, fmin, fmax, nstep)
    # plot reflection coefficient with frequency
    plt.plot(gammafreqsweep[0], gammafreqsweep[1], label=f'N = {i}')
    i += Nstep
plt.xlabel('f [GHz]')
plt.ylabel('| \u0393 |')
plt.legend()

plt.axhline(y = 0.1, color = 'r', linestyle = ':')

plt.show()