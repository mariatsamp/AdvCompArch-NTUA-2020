import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np



energy_file = "/home/mary/advcomparch_ex4/outputs/energies3_2.txt"
times_file = "/home/mary/advcomparch_ex4/outputs/times3_2.txt"


modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
topologies=["share-all","share-L3","share-nothing"]


def find_index(x,l):
	i=0;
	for el in l:
		if x==el:
			return i
		i +=1
	return -1

energy_axis = [[],[],[],[],[]]
times_axis = [[],[],[],[],[]]

fe = open(energy_file,'r')
le = fe.readline()
while le:
	tokens = le.split(' ') 
	md = tokens[0]
	topol =tokens[1]
	en = tokens[2].split('=')[1]
	
	en = float(en)
	energy_axis[find_index(md,modes)].append(en)
	le = fe.readline()
fe.close()

print("ENERGY AXIS:\n")
for ax in energy_axis:
	print(ax)
	print("\n")


ft = open(times_file,'r')
lt = ft.readline()
while lt:
	#print(lt)
	#print("\n")
	tokens = lt.split(' ') 
	md = tokens[0]
	top =tokens[1]
	t = float(tokens[3])
	times_axis[find_index(md,modes)].append(t)
	lt = ft.readline()
ft.close()


edp_axis = [[],[],[],[],[]]
for i in range(len(modes)):
	for j in range(len(topologies)):
		edp = times_axis[i][j] * energy_axis[i][j]
		edp_axis[i].append(edp)





fig, ax1 = plt.subplots()

ax1.grid(True)
ax1.set_xlabel("Topology")

xAx = np.arange(len(topologies))
ax1.xaxis.set_ticks(np.arange(0, len(topologies), 1))
ax1.set_xticklabels(topologies)
ax1.set_xlim(-1, len(topologies) + 1)

ax1.set_ylabel("Energy (J)")

colors=['red','green','blue','pink','brown']

for i in range(len(modes)):
	ax1.plot(xAx, energy_axis[i], color=colors[i],label=modes[i])

title_="Energy consumption for each topology, grainsize=1"
plt.title(title_)
plt.legend()
plt.savefig("energy_3_2.png",bbox_inches="tight")




fig, ax2 = plt.subplots()

ax2.grid(True)
ax2.set_xlabel("Topology")

xAx = np.arange(len(topologies))
ax2.xaxis.set_ticks(np.arange(0, len(topologies), 1))
ax2.set_xticklabels(topologies)
ax2.set_xlim(-1, len(topologies) + 1)

ax2.set_ylabel("EDP (J*ns)")

colors=['red','green','blue','pink','brown']

for i in range(len(modes)):
	ax2.plot(xAx, edp_axis[i], color=colors[i],label=modes[i])

title_="EDP for for each topology, grainsize=1"
plt.title(title_)
plt.legend()
plt.savefig("edp_3_2.png",bbox_inches="tight")





















