from . import constants as const


def wl_to_freq(wl):
    """ Convert wavelength (in vacuum) to frequency

    Parameters
    ----------
    wl : float
        Wavelength

    Returns
    -------
    float
        Frequency
    """
    return const.C0/wl

def freq_to_wl(freq):
    """ Convert frequency to wavelength (in vacuum)

    Parameters
    ----------
    freq : float
        Frequency

    Returns
    -------
    float
        Wavelength

    """
    return const.C0/freq
