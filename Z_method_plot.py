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
# Frequency range, I have set as 
fmin = 0
fmax = 5e9
step_by = 1000
Zn_binom = binom_design(4, 50, 300)
Zn_Z_method = z_method(4,50,300)
print("Zn binomial N=4: \n", Zn_binom, "\n")
print("Zn Z method N=4: \n", Zn_Z_method, "\n")
# Finding reflection coefficient
gammafreqsweep_z = refl_coeff_fsweep(Zn_Z_method, f0, fmin, fmax, step_by)
# plotting reflection coefficient z-method
plt.plot(gammafreqsweep_z[0], gammafreqsweep_z[1],linestyle='dotted',dashes=(2, 4),alpha=1)
# Doing same for binomial transformer
gammafreqsweep_binom = refl_coeff_fsweep(Zn_binom, f0, fmin, fmax, step_by)
plt.plot(gammafreqsweep_binom[0], gammafreqsweep_binom[1],linestyle='solid',alpha=0.25)
#Setting threshold as reflection coefficient 0.1
plt.axhline(y = 0.1, color = 'r', linestyle = ':')
plt.show()