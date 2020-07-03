#!/usr/bin/env python

import sys, os
import itertools, operator
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def get_params_from_basename(basename):
	tokens = basename.split('.')
	bench = tokens[0]
	input_size = 'simdev'
	dw = int(tokens[1].split('-')[0].split('_')[1])
	ws = int(tokens[1].split('-')[1].split('_')[1])
	return (bench, input_size, dw, ws)

def get_area_from_output_file(output_file):
	area = -999
	flag=True
	fp = open(output_file, "r")
	line = fp.readline()
	while line and flag:
		if "Area" in line:
			area = float(line.split()[2])
			flag=False
		line = fp.readline()

	fp.close()
	return area

def get_energy_from_output_file(output_file):
	energy = -999
	flag=False
	unit = "geia"
	fp = open(output_file, "r")
	line = fp.readline()
	while line:
		if "total" in line:
			energy = float(line.split()[3])
			unit = line.split()[4]
		line = fp.readline()

	fp.close()
	if unit=="mJ":
		flag = True
	return (energy,flag)

def tuples_by_dispatch_width(tuples):
	ret = []
	tuples_sorted = sorted(tuples, key=operator.itemgetter(0))
	for key,group in itertools.groupby(tuples_sorted,operator.itemgetter(0)):
		ret.append((key, list(zip(*map(lambda x: x[1:], list(group))))))
	return ret

global_ws = [16,32,64,96,128,192,256,384]
#outdir = "/home/mary/outputs/"
#path = "/home/mary/outputs/"
#benches = sys.argv[1:]
results_tuples = []

paths = ["/home/mary/outputs/astar/astar.DW_01-WS_016.out", "/home/mary/outputs/astar/astar.DW_01-WS_032.out", "/home/mary/outputs/astar/astar.DW_01-WS_064.out", "/home/mary/outputs/astar/astar.DW_01-WS_096.out", "/home/mary/outputs/astar/astar.DW_01-WS_128.out", "/home/mary/outputs/astar/astar.DW_01-WS_192.out", "/home/mary/outputs/astar/astar.DW_01-WS_256.out", "/home/mary/outputs/astar/astar.DW_01-WS_384.out", "/home/mary/outputs/astar/astar.DW_02-WS_016.out", "/home/mary/outputs/astar/astar.DW_02-WS_032.out", "/home/mary/outputs/astar/astar.DW_02-WS_064.out", "/home/mary/outputs/astar/astar.DW_02-WS_096.out", "/home/mary/outputs/astar/astar.DW_02-WS_128.out", "/home/mary/outputs/astar/astar.DW_02-WS_192.out", "/home/mary/outputs/astar/astar.DW_02-WS_256.out", "/home/mary/outputs/astar/astar.DW_02-WS_384.out", "/home/mary/outputs/astar/astar.DW_04-WS_016.out", "/home/mary/outputs/astar/astar.DW_04-WS_032.out", "/home/mary/outputs/astar/astar.DW_04-WS_064.out", "/home/mary/outputs/astar/astar.DW_04-WS_096.out", "/home/mary/outputs/astar/astar.DW_04-WS_128.out", "/home/mary/outputs/astar/astar.DW_04-WS_192.out", "/home/mary/outputs/astar/astar.DW_04-WS_256.out", "/home/mary/outputs/astar/astar.DW_04-WS_384.out", "/home/mary/outputs/astar/astar.DW_08-WS_016.out", "/home/mary/outputs/astar/astar.DW_08-WS_032.out", "/home/mary/outputs/astar/astar.DW_08-WS_064.out", "/home/mary/outputs/astar/astar.DW_08-WS_096.out", "/home/mary/outputs/astar/astar.DW_08-WS_128.out", "/home/mary/outputs/astar/astar.DW_08-WS_192.out", "/home/mary/outputs/astar/astar.DW_08-WS_256.out", "/home/mary/outputs/astar/astar.DW_08-WS_384.out", "/home/mary/outputs/astar/astar.DW_16-WS_016.out", "/home/mary/outputs/astar/astar.DW_16-WS_032.out", "/home/mary/outputs/astar/astar.DW_16-WS_064.out", "/home/mary/outputs/astar/astar.DW_16-WS_096.out", "/home/mary/outputs/astar/astar.DW_16-WS_128.out", "/home/mary/outputs/astar/astar.DW_16-WS_192.out", "/home/mary/outputs/astar/astar.DW_16-WS_256.out", "/home/mary/outputs/astar/astar.DW_16-WS_384.out", "/home/mary/outputs/astar/astar.DW_32-WS_032.out", "/home/mary/outputs/astar/astar.DW_32-WS_064.out", "/home/mary/outputs/astar/astar.DW_32-WS_096.out", "/home/mary/outputs/astar/astar.DW_32-WS_128.out", "/home/mary/outputs/astar/astar.DW_32-WS_192.out", "/home/mary/outputs/astar/astar.DW_32-WS_256.out", "/home/mary/outputs/astar/astar.DW_32-WS_384.out"]

for dirname in paths:
	if dirname.endswith("/"):
		dirname = dirname[0:-1]
	basename = os.path.basename(dirname)
	output_file = dirname + "/power.txt"

	(bench, input_size, dispatch_width, window_size) = get_params_from_basename(basename)
	area = get_area_from_output_file(output_file)
	if window_size >= 16:
		results_tuples.append((dispatch_width, window_size, area))


markers = ['.', 'o', 'v', '*', 'D']
fig = plt.figure()
plt.grid(True)
ax = plt.subplot(111)
ax.set_xlabel("Window Size")
ax.set_ylabel("Chip Size (mm^2)")

i = 0
tuples_by_dw = tuples_by_dispatch_width(results_tuples)
for tuple in tuples_by_dw:
	dw = tuple[0]
	ws_axis = tuple[1][0]
	ipc_axis = tuple[1][1]
	x_ticks = np.arange(0, len(global_ws))
	if (i>=5) :
		ipc_axis = (np.nan,) + ipc_axis
	x_labels = map(str, global_ws)
	ax.xaxis.set_ticks(x_ticks)
	ax.xaxis.set_ticklabels(x_labels)

	ax.plot(x_ticks, ipc_axis, label="DW_"+str(dw), marker=markers[i%len(markers)])
	i = i + 1

plt.title("chip size of astar" , fontsize=12)
lgd = ax.legend(ncol=len(tuples_by_dw), bbox_to_anchor=(0.9, -0.1), prop={'size':8})
plt.savefig(bench+'-'+"chip" +'.ipc.png', bbox_extra_artists=(lgd,), bbox_inches='tight')
