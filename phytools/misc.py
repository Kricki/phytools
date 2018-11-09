import numpy as np


def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx], idx


def moving_average_filter(signal, taps):
    """ Apply moving average filter.
    See http://www.analog.com/media/en/technical-documentation/dsp-book/dsp_book_Ch15.pdf

    Parameters
    ----------
    signal : nd.array
        The signal to be filtered
    taps : int
        Width of filter window

    Returns
    -------
    nd.array
        Filtered output signal

    """
    filter_window = np.ones(taps)/taps
    output = np.convolve(signal, filter_window, 'same')
    return output