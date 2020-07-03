import sys
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats

def findindex(x,L):
	for i in range(len(L)):
		if L[i]==x:
			return i
	return -1


path = '/home/mary/outputsSize/'
DW = ['01','02','04','08','16','32']
WS = ['016','032','064','096','128','192','256','384']
SIZE_AXIS_DW_01 = []
SIZE_AXIS_DW_02 = []
SIZE_AXIS_DW_04 = []
SIZE_AXIS_DW_08 = []
SIZE_AXIS_DW_16 = []
SIZE_AXIS_DW_32 = []


filename=path+"gobmk.size"
fp = open(filename,"r")

line = fp.readline()
while line:
	if line.startswith('DW_01'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_01.append(size)
	elif line.startswith('DW_02'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_02.append(size)
	elif line.startswith('DW_04'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_04.append(size)
	elif line.startswith('DW_08'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_08.append(size)
	elif line.startswith('DW_16'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_16.append(size)
	elif line.startswith('DW_32'):
		size=float(line.split()[1])
		ws=line.split()[0].split('_')[2]
		SIZE_AXIS_DW_32.append(size)
	line = fp.readline()
	line = fp.readline()

fig, ax1 = plt.subplots()
ax1.grid(True)
ax1.set_xlabel("Window_Size")
xAx = np.arange(len(WS))
ax1.xaxis.set_ticks(np.arange(0, len(WS), 1))
ax1.set_xticklabels(WS)
ax1.set_ylabel("Size (mm^2)")
ax1.grid(True)

print(SIZE_AXIS_DW_01)
print(SIZE_AXIS_DW_02)
print(SIZE_AXIS_DW_04)
print(SIZE_AXIS_DW_08)
print(SIZE_AXIS_DW_16)
print(SIZE_AXIS_DW_32)

l1 = ax1.plot(xAx, SIZE_AXIS_DW_01, color='blue',label='DW=01')
l2 = ax1.plot(xAx, SIZE_AXIS_DW_02, color='orange',label='DW=02')
l3 = ax1.plot(xAx, SIZE_AXIS_DW_04, color='green',label='DW=04')
l4 = ax1.plot(xAx, SIZE_AXIS_DW_08, color='red',label='DW=08')
l5 = ax1.plot(xAx, SIZE_AXIS_DW_16, color='purple',label='DW=16')
l6 = ax1.plot(xAx[1:], SIZE_AXIS_DW_32[1:], color='brown',label='DW=32')

plt.title("Circuit Board Size")
plt.legend()
plt.savefig("size",bbox_inches="tight")



























