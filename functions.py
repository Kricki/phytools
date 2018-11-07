import numpy as np


def gaussian(x, a, x0, fwhm, offset):
    """ Compute Gaussian function.
    http://mathworld.wolfram.com/GaussianFunction.html

    Parameters
    ----------
    x : parameter at which the Gaussian function is computed
    a : amplitude
    x0 : offset on x-axis
    fwhm : Full-width-at-half-maximum (FWHM)
    offset : amplitude offset

    Returns
    -------
    float
        Value of Gaussian function for x

    """
    s = fwhm/(2*np.sqrt(2*np.log(2)))
    return a*np.exp(-(x-x0)**2/(2*s**2)) + offset


def lorentzian(x, a, x0, fwhm, offset):
    """ Compute Lorentzian function.
    http://mathworld.wolfram.com/LorentzianFunction.html
    The function is normalized not to its area, but to the amplitude a.

    Parameters
    ----------
    x : float
        parameter at which the Lorentzian function is computed
    a : float
        amplitude
    x0 : float
        offset on x-axis
    fwhm : float
        Full-width-at-half-maximum (FWHM)
    offset : float
        amplitude offset

    Returns
    -------
    float
        Value of Lorentzian function for x

    """
    return a*fwhm**2/4/((x-x0)**2 + (fwhm/2)**2) + offset


#def airy_fpi(length, wl, finesse):
#    delta = 4*np.pi*length/wl
#    return 1/(1+finesse*np.sin(delta/2)**2)

def airy_fpi(delta, r1, r2):
    """ Compute Airy function of a Fabry-Perot interferometer

    Parameters
    ----------
    delta : float
        Round-trip phase inside the cavity (in radians)
    r1 : Reflection coefficient (field value) for mirror 1
    r2 : Reflection coefficient (field value) for mirror 1

    Returns
    -------
    float
        Value of Airy function

    """
    #delta = 4*np.pi*length/wl  # round-trip phase shift
    f = 4*r1*r2/(1-r1*r2)**2  # f: "finesse coefficient", note: finesse=pi*sqrt(f)/2=pi*sqrt(r1*r2)/(1-r1*r2)
    #a = 1/(1-r1*r2)**2
    a = r1*r2
    #a=1
    return a/(1+f*np.sin(delta/2)**2)


def scale(value, mode):
    """ Scale value

    Parameters
    ----------
    value : float or array-like
        Value or array to be scaled
    mode : str
        'log': scale to log10(value)*10
        'linear': scale to linear from log10

    Returns
    -------
    float or array-like
        Scaled value
    """
    if mode == 'linear':
        return 10**(value/10)
    elif mode == 'log':
        return np.log10(value) * 10
