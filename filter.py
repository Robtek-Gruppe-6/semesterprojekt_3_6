from scipy.signal import butter, lfilter, freqz, filtfilt #butterworth filter
from scipy.fft import fft, fftfreq #Fast Fourirer transfrom
import numpy as np

class Filter:
    def __init__(self, order = 6, rate=44100, cutoff=625, stopoff=1800): 
        # Default filter order can be overridden
        self.order = order #Default order is set to 6
        self.rate = rate # Sample rate
        self.cutoff = cutoff #High pass cutoff frequency (slighlty lower than the lowest dtmf tone)
        self.stopoff = stopoff #Stopoff for bandpass


    #Bandpass filter using Butterworth design
    def butter_bandpass(self, data): 
        nyquist = 0.5 * self.rate
        high = self.stopoff / nyquist
        low = self.cutoff / nyquist
        b, a = butter(self.order,[low, high], btype='bandpass')
        filtered_data = lfilter(b,a,data)
        return filtered_data

    #Frequency analysis using FFT
    def analyze_frequency(self, data):
        window = np.hamming(len(data))
        data_windowed = data * window
        N = len(data_windowed)
        yf = fft(data_windowed)
        xf = fftfreq(N, 1 / self.rate)

        positive_frequencies = xf[:N // 2]
        magnitude = np.abs(yf[:N // 2])

        return positive_frequencies, magnitude
    
fil = Filter() #Laver instans til main