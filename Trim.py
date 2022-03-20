shelf = 25000
preClickEcho = 500
clickEcho = 10000

trimmedSignal = []
i = 0
while i < len(signal):
    s = signal[i]
    if (-1 * shelf) < s > shelf:
            trimmedSignal = trimmedSignal[0:i - preClickEcho]
            i += clickEcho
            while i < len(signal) and (-1 * shelf) < signal[i] < shelf:
                i += 1
            i += clickEcho
    else:
        trimmedSignal.append(s)
        i += 1


plt.figure(1)
plt.xlim(0, 300000)
plt.title("Original Signal")
plt.ylim(-50000, 50000)
plt.plot(signal)


plt.figure(2)
plt.title("Without the section between clicks")
plt.plot(trimmedSignal)
plt.xlim(0, 300000)
plt.ylim(-50000, 50000)

plt.show()