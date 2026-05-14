# Emg script 4/4, On set Detection.

# This script detects when muscle activity starts and stops. It is called On Set Detection.
# It uses the first 500 samples to establish a baseline, computes a threshold and
# uses that to detect every moment that the rectified EMG signal goes above it.
# Upward it Onset, and downward is offset.

# execfile ("Emg3_FileredRectifyPlot.py") exec and read the third file
exec(open("Emg3_FileredRectifyPlot.py").read())

rest_segment = emg_rectified[:500]
activation_threshold = np.mean(rest_segment) + 3 * np.std(rest_segment)

# Here it uses the emg_rectified and slices the first 500 initial samples, so
# it contains only noise and no muscle activity. It is a reference for what the signal looks like when it is at rest.
# The threshold is mean + 3 deviations, so anything else is real muscle activity.

above_threshold = emg_rectified > threshold

# This produces a boolean array that each time that a sample exceeds the threshold, it is a true.

onsets  = np.where(np.diff(above_threshold.astype(int)) == 1)[0]
offsets = np.where(np.diff(above_threshold.astype(int)) == -1)[0]

# Here we converts the boolean array to integers, so it looks from 
# [false, false, true, true, true, ...] to [0, 0, 1, 1, 1, ...]
# np.diff computes the difference. 0 -> 1 = +1, 1 -> = -1

figure = plt.figure()
plt.plot(time_vector, emg_rectified, label='Rectified EMG')
plt.axhline(threshold, color='r', linestyle='--', label='Threshold')
for on in onsets:
    plt.axvline(time_vector[on], color='g', linestyle='--', label='Onset' if on == onsets[0] else '')
for off in offsets:
    plt.axvline(time_vector[off], color='orange', linestyle='--', label='Offset' if off == offsets[0] else '')
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.legend()
fig.set_size_inches(w=11, h=7)
fig.savefig('OnSetDetection.png')