import numpy as np
from scipy import optimize
from scipy import integrate


def maxwell(v):
    return 4/np.sqrt(np.pi)*v**2*np.exp(-v**2)


def functionForc(v):
    return integrate.quad(maxwell, 0, v)[0] - 1/2


def functionFord(v):
    return v**2*np.exp(-v**2) - 1/(2*np.exp(1))


#c)
print(optimize.brentq(functionForc, 0, 3))
#d)
v_left = optimize.brentq(functionFord, 0, 1)  # Find the left value for which f(v)=f(v_m)/2
v_right = optimize.brentq(functionFord, 1, 2)  # Find the right value for which f(v)=f(v_m)/2
print(v_right - v_left)
