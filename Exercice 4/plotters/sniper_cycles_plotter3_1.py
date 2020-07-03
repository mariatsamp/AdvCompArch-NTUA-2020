import sys, os
import itertools, operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

#CHANGE THIS ONE ACCORDING TO YOUR OUTPUT PATH
outpath="/home/mary/advcomparch_ex4/outputs"

#CHANGE THIS TO "1", "10", "100" AND EXECUTE FOR EACH ONE
gs="100"

nthreads=[1,2,4,8,16]
modes=["TAS_CAS","TAS_TS","TTAS_CAS","TTAS_TS","MUTEX"]

cycles_axis = [[],[],[],[],[]]


for i in range(len(modes)):
	for n in nthreads:
		file1=outpath+"/3_1/"+modes[i]+"/"+str(n)+"_threads/"+"threads_"+str(n)+"_grainsize_"+gs+"/sim.out"
		fp = open(file1)
		#print("ok")
		line=fp.readline()
		while line:
			if line.startswith("  Cycles"):
				tokens=line.split()
				cycles=int(tokens[2])
				cycles_axis[i].append(cycles)
				#print("Added value "+ cycles + " to list " + modes[i])
				break
			line = fp.readline()
		
	print("MODE: "+modes[i])
	print(cycles_axis[i])

fig, ax = plt.subplots()

ax.grid(True)
ax.set_xlabel("number of threads")

xAx = np.arange(len(nthreads))
ax.xaxis.set_ticks(np.arange(0, len(nthreads), 1))
ax.set_xticklabels(nthreads)
ax.set_xlim(-1, len(nthreads) + 1)

ax.set_ylabel("Number of cycles")

colors=['red','green','blue','pink','brown']

for i in range(len(modes)):
	ax.plot(xAx, cycles_axis[i], color=colors[i],label=modes[i])

#for i in [2,3,4]:
#	ax.plot(xAx, cycles_axis[i], color=colors[i],label=modes[i])
title_="Grainsize: "+ gs
plt.title(title_)
plt.legend()
plt.savefig("grainsize_"+gs+".png",bbox_inches="tight")

