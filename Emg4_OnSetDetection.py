exec(open("Emg3_FileredRectifyPlot.py").read())

# definir limiar no repouso inicial = primeiras 500 amostras de sinal
baseline = emg_rectified[:500]
threshold = np.mean(baseline) + 3 * np.std(baseline) # limiar = media + 3 desvios padrao

# detectar cruzamentos do limiar
above_threshold = emg_rectified > threshold

# onset = transicao de False para True (0->1)
# offset = transicao de True para False (1->0)
onsets  = np.where(np.diff(above_threshold.astype(int)) == 1)[0]
offsets = np.where(np.diff(above_threshold.astype(int)) == -1)[0]

# plotar grafico
fig = plt.figure()
plt.plot(time, emg_rectified, label='EMG retificado')
plt.axhline(threshold, color='r', linestyle='--', label='Limiar')
for on in onsets:
    plt.axvline(time[on], color='g', linestyle='--', label='Onset' if on == onsets[0] else '')
for off in offsets:
    plt.axvline(time[off], color='orange', linestyle='--', label='Offset' if off == offsets[0] else '')
plt.xlabel('Time (sec)')
plt.ylabel('EMG (a.u.)')
plt.legend()
fig.set_size_inches(w=11, h=7)
fig.savefig('fig5.png')