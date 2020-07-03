import sys, os

energy_path = "/home/mary/advcomparch_ex4/mcpat_outputs/3_1"


fwrite = open("/home/mary/advcomparch_ex4/outputs/energies3_1.txt", "w")
modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
nthreads = ["1","2","4","8","16"]

for md in modes:
	for n in nthreads:
		for gs in ["1", "10", "100"]:
			pathfile = energy_path+"/"+md+"/"+n+"_threads"+"/threads_"+n+"_grainsize_"+gs+"/energy.total"
			fp = open(pathfile,'r')
			line = fp.readline()
			while line:
				if line.startswith("  total"):
					tokens = line.split()
		    			energy = float(tokens[3])
					if tokens[4] == "kJ":
						energy *= 1000;
		    			#bench = file.split("/")[6].split(".")[1]
		   			print(md+", "+n+" Threads,"+gs+" Grainsize: Energy =" + str(energy))
					fwrite.write(md+", "+n+" Threads,"+gs+" Grainsize: Energy =" + str(energy)+"\n") 
				    	break
				line = fp.readline()
			fp.close()
fwrite.close()
				


    
            
