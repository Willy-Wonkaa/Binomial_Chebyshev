import numpy
from Transfomer_design import *
from plotrefl import *
#Importing matplotlib
import matplotlib.pyplot as plt
#central frequency f0b set at 2.5 GHz, light speed in vacuum, central wavelength (at f0), physical length of each section
f0 = 2.5e9
c = 3e8
lambda0 = c/f0
sect_length = lambda0/4
# Grequency range, I have set as 
fmin = 0
fmax = 5e9
step_by = 1000
Zn_binom = binom_design(4, 50, 300)
Zn_cheb_rhom005 = chebyshev_4()
print("Zn binomial N=4: \n", Zn_binom, "\n")
print("Zn Chebyshev N=4: \n", Zn_cheb_rhom005, "\n")
# Finding reflection coefficient
gammafreqsweep_cheb = refl_coeff_fsweep(Zn_cheb_rhom005, f0, fmin, fmax, step_by)
# plotting reflection coefficient chebyshev transformer
plt.plot(gammafreqsweep_cheb[0], gammafreqsweep_cheb[1])
# Doing same for binomial transformer
gammafreqsweep_binom = refl_coeff_fsweep(Zn_binom, f0, fmin, fmax, step_by)
plt.plot(gammafreqsweep_binom[0], gammafreqsweep_binom[1])
# print(bandwidth_cheb)
plt.axhline(y = 0.1, color = 'r', linestyle = ':')
plt.show()



