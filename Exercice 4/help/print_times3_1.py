import sys, os

outpath = "/home/mary/advcomparch_ex4/outputs/3_1"


fwrite = open("/home/mary/advcomparch_ex4/outputs/times3_1.txt", "w")
modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
nthreads = ["1","2","4","8","16"]

for md in modes:
	for n in nthreads:
		for gs in ["1", "10", "100"]:
			pathfile = outpath+"/"+md+"/"+n+"_threads"+"/threads_"+n+"_grainsize_"+gs+"/sim.out"
			fp = open(pathfile,'r')
			line = fp.readline()
			while line:
				if line.startswith("  Time"):
					tokens = line.split()
		    			t = float(tokens[3])
		    			#bench = file.split("/")[6].split(".")[1]
		   			print(md+", "+n+" Threads,"+gs+" Grainsize: Time =" + str(t))
					fwrite.write(md+", "+n+" Threads,"+gs+" Grainsize: Time =" + str(t)+" (ns)"+"\n") 
				    	break
				line = fp.readline()
			fp.close()
fwrite.close()
				


    
            
