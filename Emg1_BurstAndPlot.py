# Emg script 1/4, Burst And Plot.

"""
This script is mainly used to synthetically generate an EMG signal.
It does that by concatenating quiet and active segments (resting and burst muscle activity),
then plots and saves the result as an image. There is no real sensor data,
it is purely for demonstration or testing purposes.
"""

# Here, we import two heavily important python libraries, numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

"""
Imports numpy and creates an alias for it, so every time we call "np", we are calling numpy lib.
The same applies to matplotlib as plt.
Numpy is a library that adds support for large and multi-dimensional arrays and matrices,
and a large collection of high-level mathematical functions to operate on them.
Matplotlib, as the name suggests, is a plotting library and it is a numerical Numpy extension.
"""

# Here, we simulate all the EMGs signals that we are going to plot and use
dc_offset = 0.08
active_segment_1 = np.random.uniform(-1, 1, size=1000) + dc_offset
active_segment_2 = np.random.uniform(-1, 1, size=1000) + dc_offset
rest_segment = np.random.uniform(-0.05, 0.05, size=500) + dc_offset
emg_signal = np.concatenate([rest_segment, active_segment_1, rest_segment, active_segment_2, rest_segment])

"""
np.random.uniform(low, high, size) is a command that generates "size" random samples,
distributed between low and high numbers. So for burst1 and 2, we are asking for 1000 samples,
between -1 and 1. The + 0.08 constant is a baseline to every sample, simulating a small noise
and prevent it to be zero, like real-world muscles.  
quiet variable asks for the same thing, but it wants samples between -0.05 and 0.05, 
simulating a resting muscle without any movement.

The emg array is assembled to simulate a muscle: 
rest -> burst1 -> rest -> burst2 -> rest
"""
# Here, we have time axis
sampling_rate = 1000 # Hz
time_vector = np.arange(len(emg_signal)) / sampling_rate

"""
This builds a time vector that corresponds to each sample in the signal.
The sampling rate 1000 means that 1000 samples are recorded per second, so the
time interval of each sample is 1/1000 = 0.001 seconds. It has the same length as emg_signal,
where each value represents time axis.
"""

# Here, we plot and save the information
plot_filename = 'BurstAndPlotGraph.png'
figure = plt.figure()
plt.plot(time_vector, emg_signal)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
figure.set_size_inches(w=11,h=7)
figure.savefig(plot_filename)

"""
This defines the name of the image and plots time_vector as x and emg_signal as y.
On x label it gives the "Time (sec)" name, and in y label "EMG (a.u.)", arbitrary units.
"""