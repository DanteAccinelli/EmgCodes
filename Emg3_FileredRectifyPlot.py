# Emg script 3/4, Filter and Rectify.

# This script introduces two preprocessing EMG steps: bandpass filtering and rectification.
# It produces two comparison plots afterwards.

# execfile ("Emg2_CorrectMeanPlot.py") exec and read the second file
exec(open("Emg2_CorrectedMeanPlot.py").read())

import scipy as sp
from scipy import signal

# Scipy is another library built on top of numpy, so it extends its math capabilities.
# signal is a submodule of scipy that works with signal processing, filters and more.

# create bandpass filter for EMG
sampling_rate = 1000 # Hz
low_cutoff_hz = 20 # Hz
high_cutoff_hz = 450 # Hz
low_cutoff_normalized = low_cutoff_hz/(sampling_rate/2)
high_cutoff_normalized = high_cutoff_hz/(sampling_rate/2)
b, a = sp.signal.butter(4, [low_cutoff_normalized, high_cutoff_normalized], btype='bandpass')

# 1000/2 is the Nyquist frequency, half of the sampling rate. So 20 (1000/2)
# is 20Hz as a Nyquist fraction for high, and 450Hz for low. These are the standard rate.
# sp.signal.butter is a Butterworth bandpass filter of order 4.

# process EMG signal: filter EMG
emg_filtered = sp.signal.filtfilt(b, a, emg_mean_corrected)

# filtfilt applies the filter twice, once foward and once backward. This cancels the
# phase distortion.

# plot comparison of unfiltered vs filtered mean-corrected EMG
comparison_figure = plt.figure()
plt.subplot(1, 2, 1)
plt.subplot(1, 2, 1).set_title('Unfiltered EMG')
plt.plot(time_vector, emg_mean_corrected)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

plt.subplot(1, 2, 2)
plt.subplot(1, 2, 2).set_title('Filtered EMG')
plt.plot(time_vector, emg_filtered)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

comparison_figure.tight_layout()
plot_filename = 'UnfilteredVsFiltered.png'
comparison_figure.set_size_inches(w=11,h=7)
comparison_figure.savefig(plot_filename)

# First comparison.

# process EMG signal: rectify
emg_rectified = abs(emg_filtered)

# EMG signal oscilalte around zero, so muscle activity produces positive and
# negative numbers. To measure the magnitude, we take the absolute value of the samples,
# with a full-wave rectification.
# After this, the signal is always non-negative.

# plot comparison of unrectified vs rectified EMG
comparison_figure = plt.figure()
plt.subplot(1, 2, 1)
plt.subplot(1, 2, 1).set_title('Unrectified EMG')
plt.plot(time_vector, emg_filtered)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

plt.subplot(1, 2, 2)
plt.subplot(1, 2, 2).set_title('Rectified EMG')
plt.plot(time_vector, emg_rectified)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

comparison_figure.tight_layout()
plot_filename = 'UnrectifiedVsRectified.png'
comparison_figure.set_size_inches(w=11,h=7)
comparison_figure.savefig(plot_filename)

# Second Comparison.