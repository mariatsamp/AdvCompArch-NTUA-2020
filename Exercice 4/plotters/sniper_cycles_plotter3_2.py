import sys, os
import itertools, operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#CHANGE THIS ONE ACCORDING TO YOUR OUTPUT PATH
outpath="/home/chvd/advcomparch_ex4/outputs"



topologies=["share-all","share-L3","share-nothing"]


modes=["TAS_CAS","TAS_TS","TTAS_CAS","TTAS_CAS","MUTEX"]

cycles_axis = [[],[],[],[],[]]



for i,m in enumerate(modes):
	for t in topologies:
		file1=outpath+"/3_2/"+t+"/"+m+"/sim.out"
		fp = open(file1)
		#print("ok")
		line=fp.readline()
		while line:
			if line.startswith("  Cycles"):
				tokens=line.split()
				cycles=int(tokens[2])
				cycles_axis[i].append(cycles)
				break
			line = fp.readline()
		
	print("MODE: "+modes[i])
	print(cycles_axis[i])

fig, ax = plt.subplots()

ax.grid(True)
ax.set_xlabel("Topology type (4 threads, 4 cores)")

xAx = np.arange(len(topologies))
ax.xaxis.set_ticks(np.arange(0, len(topologies), 1))
ax.set_xticklabels(topologies)
ax.set_xlim(-1, len(topologies) + 1)

ax.set_ylabel("Number of cycles")

colors=['red','green','blue','pink','brown']

for i in range(len(modes)):
	ax.plot(xAx, cycles_axis[i], color=colors[i],label=modes[i])

#for i in [2,3,4]:
#	ax.plot(xAx, cycles_axis[i], color=colors[i],label=modes[i])
title_="Cycles for each combination of Topology-Mode"
plt.title(title_)
plt.legend()
plt.savefig("3_2.png",bbox_inches="tight")

