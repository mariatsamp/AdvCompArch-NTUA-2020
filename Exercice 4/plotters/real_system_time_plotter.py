import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np




times_file = "/home/mary/advcomparch_ex4/outputs/real_system_times.txt"


modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
nthreads = [1,2,4]
GR="1"

def find_index(x,l):
	i=0;
	for el in l:
		if x==el:
			return i
		i +=1
	return -1

times_axis = [[],[],[],[],[]]



for i,mode in enumerate(modes):
	fp = open(times_file,'r')
	mode_found=False
	line = fp.readline()
	while line:
		if line.startswith(mode):
			print("found " + mode)
			ctr = 3
			break
		line = fp.readline()
	line = fp.readline()
	while line and ctr>0:
		if line.startswith("Nthreads"):
			gs = line.split()[4]
			print("grainsize="+gs)
			if gs == GR:
				print("OK")
				line=fp.readline()
				time = line.split(':')[1]
				time = time.split()[0]
				times_axis[i].append(float(time))
				ctr -= 1
		line = fp.readline()
				
	fp.close()


		




print("TIME AXIS:\n")
for ax in times_axis:
	print(ax)
	print("\n")

fig, ax1 = plt.subplots()

ax1.grid(True)
ax1.set_xlabel("number of threads")

xAx = np.arange(len(nthreads))
ax1.xaxis.set_ticks(np.arange(0, len(nthreads), 1))
ax1.set_xticklabels(nthreads)
ax1.set_xlim(-1, len(nthreads) + 1)

ax1.set_ylabel("Time(s)")

colors=['red','green','blue','pink','brown']

for i in range(len(modes)):
	ax1.plot(xAx, times_axis[i], color=colors[i],label=modes[i])

title_="Real System Time for Grainsize = "+ GR
plt.title(title_)
plt.legend()
plt.savefig("user_system_times_gainsize_"+GR+".png",bbox_inches="tight")

























