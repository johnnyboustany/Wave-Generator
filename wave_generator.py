import numpy as np
import matplotlib.pyplot as plt
import pyaudio

p = pyaudio.PyAudio()

volume = 0.5     # range [0.0, 1.0]
fs = 41000       # sampling rate, Hz, must be integer
duration = 10   # in seconds, may be float
f = 1000      # sine frequency, Hz, may be float

time_array = np.arange(fs*duration)

function = np.sin(2*np.pi*time_array*f/fs).astype(np.float32)

# fspaces = np.linspace(500,1000,10)
# freqs = np.repeat(fspaces, repeats = len(time_array) / 10)
# len(time_array)
# len(freqs)
# function_s = np.sin(2*np.pi*time_array * 500 / fs).astype(np.float32)
# function = np.sin(2*np.pi*time_array * freqs / fs).astype(np.float32)
# function_e = np.sin(2*np.pi*time_array * 1000 / fs).astype(np.float32)
# function2 = np.sin(2*np.pi*time_array2).astype(np.float32)

# plt.plot(freqs)

# plt.plot(function)
# plt.xlim([0,1000])
# output = np.concatenate([function,function2])


# plt.plot(function)
#
# # plt.plot(function_e)
# time_array.shape

# plt.plot(function2)
# plt.plot(function)
# plt.xlim([0,1000])

# # generate samples, note conversion to float32 array
# samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)
# samples = (np.arange(fs*duration))*np.

# for paFloat32 sample values must be in range [-1.0, 1.0]
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=fs,
                output=True)

# play. May repeat with different volume values (if done interactively)
# stream.write(volume*function_s)
stream.write(volume*function)
# stream.write(volume*function_e)
# stream.write(volume*function2)

stream.stop_stream()
stream.close()

p.terminate()
