import sys
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

def findindex(x,L):
	for i in range(len(L)):
		if L[i]==x:
			return i
	return -1


path = '/home/mary/outputsEnergy/'
DW = ['01','02','04','08','16','32']
WS = ['016','032','064','096','128','192','256','384']
BENCHMARKS = ['astar','cactusADM','gcc','GemsFDTD','gobmk','hmmer','mcf','omnetpp','sjeng','soplex','xalancbmk','zeusmp']
ENERGY_AXIS_DW_01 = [[],[],[],[],[],[],[],[]]
ENERGY_AXIS_DW_02 = [[],[],[],[],[],[],[],[]]
ENERGY_AXIS_DW_04 = [[],[],[],[],[],[],[],[]]
ENERGY_AXIS_DW_08 = [[],[],[],[],[],[],[],[]]
ENERGY_AXIS_DW_16 = [[],[],[],[],[],[],[],[]]
ENERGY_AXIS_DW_32 = [[],[],[],[],[],[],[],[]]

for bench in BENCHMARKS:
	filename=path+bench+".consumption"
	fp = open(filename,"r")
	print("processing "+bench)
	line = fp.readline()
	while line:
		if line.startswith('DW_01'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_01[findindex(ws,WS)].append(energy)
		elif line.startswith('DW_02'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_02[findindex(ws,WS)].append(energy)
		elif line.startswith('DW_04'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_04[findindex(ws,WS)].append(energy)
		elif line.startswith('DW_08'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_08[findindex(ws,WS)].append(energy)
		elif line.startswith('DW_16'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_16[findindex(ws,WS)].append(energy)
		elif line.startswith('DW_32'):
			energy=float(line.split()[1])
			ws=line.split()[0].split('_')[2]
			ENERGY_AXIS_DW_32[findindex(ws,WS)].append(energy)
		line = fp.readline()

fig, ax1 = plt.subplots()
ax1.grid(True)
ax1.set_xlabel("Window_Size")
xAx = np.arange(len(WS))
ax1.xaxis.set_ticks(np.arange(0, len(WS), 1))
ax1.set_xticklabels(WS)
ax1.set_ylabel("Energy(J)")
ax1.grid(True)

for i in range(8):
	#ENERGY_AXIS_DW_01[i] = stats.mstats.gmean(ENERGY_AXIS_DW_01[i])
	#ENERGY_AXIS_DW_02[i] = stats.mstats.gmean(ENERGY_AXIS_DW_02[i])
	#ENERGY_AXIS_DW_04[i] = stats.mstats.gmean(ENERGY_AXIS_DW_04[i])
	#ENERGY_AXIS_DW_08[i] = stats.mstats.gmean(ENERGY_AXIS_DW_08[i])
	#ENERGY_AXIS_DW_16[i] = stats.mstats.gmean(ENERGY_AXIS_DW_16[i])
	#ENERGY_AXIS_DW_32[i] = stats.mstats.gmean(ENERGY_AXIS_DW_32[i])

	ENERGY_AXIS_DW_01[i] = np.mean(ENERGY_AXIS_DW_01[i])
	ENERGY_AXIS_DW_02[i] = np.mean(ENERGY_AXIS_DW_02[i])
	ENERGY_AXIS_DW_04[i] = np.mean(ENERGY_AXIS_DW_04[i])
	ENERGY_AXIS_DW_08[i] = np.mean(ENERGY_AXIS_DW_08[i])
	ENERGY_AXIS_DW_16[i] = np.mean(ENERGY_AXIS_DW_16[i])
	ENERGY_AXIS_DW_32[i] = np.mean(ENERGY_AXIS_DW_32[i])
	

l1 = ax1.plot(xAx, ENERGY_AXIS_DW_01, color='cyan',label='DW=01')
l2 = ax1.plot(xAx, ENERGY_AXIS_DW_02, color='orange',label='DW=02')
l3 = ax1.plot(xAx, ENERGY_AXIS_DW_04, color='green',label='DW=04')
l4 = ax1.plot(xAx, ENERGY_AXIS_DW_08, color='red',label='DW=08')
l5 = ax1.plot(xAx, ENERGY_AXIS_DW_16, color='purple',label='DW=16')
l6 = ax1.plot(xAx[1:], ENERGY_AXIS_DW_32[1:], color='brown',label='DW=32')

plt.title("Average Energy Consumed")
plt.legend()
plt.savefig("Energy gmean 2",bbox_inches="tight")



























