# Emg script 2/4, Correct Mean and Plot.

# This script builds on the first. It loads the emg_signal, applies 
# a basic preprocessing step and plots a comparison.
# It is used to remove the DC offset (mean) from the emg_signal and compares 
# with the original using a two-panel plot.


#execfile ("Emg1_BurstAndPlot.py") exec and read the first file
exec(open("Emg1_BurstAndPlot.py").read())

# Here we open the previous file and executes it in this scope, so we are
# able to import all variables to this session.

# process EMG signal: remove mean
emg_mean_corrected = emg_signal - np.mean(emg_signal)

# np.mean(emg_signal) computes the average value of the entire signal,
# wich is around 0.08 due to the constant DC offset value and subtracts it from
# every sample. This is called DC offset removal or mean subtraction.

# plot comparison of EMG with offset vs mean corrected values
comparison_figure = plt.figure()
plt.subplot(1, 2, 1).set_title('Mean offset present')
plt.plot(time_vector, emg_signal)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

plt.subplot(1, 2, 2).set_title('Mean-corrected values')
plt.plot(time_vector, emg_mean_corrected)
plt.locator_params(axis='x', nbins=4)
plt.locator_params(axis='y', nbins=4)
plt.ylim(-1.5, 1.5)
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')

# plt.subplot(rows, cols, index) divides everything into a grid. The index 1
# stands for the plot with offset, and the index 2 without it.
# plt.locator_params(axis = x, nbins = 4) limits the tick marks on each axis.

comparison_figure.tight_layout()
plot_filename = 'CorrectedMeanPlot.png'
comparison_figure.set_size_inches(w=11,h=7)
comparison_figure.savefig(plot_filename)


# Then we plot again.