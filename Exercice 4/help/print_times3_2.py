import sys, os

outpath = "/home/mary/advcomparch_ex4/outputs/3_2"


fwrite = open("/home/mary/advcomparch_ex4/outputs/times3_2.txt", "w")
modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
topologies = ["share-all","share-L3","share-nothing"]

for md in modes:
	for topology in topologies:
	
		pathfile = outpath+"/"+topology+"/"+md+"/sim.out"
		fp = open(pathfile,'r')
		line = fp.readline()
		while line:
			if line.startswith("  Time"):
				tokens = line.split()
	    			t = tokens[3]
	    			#bench = file.split("/")[6].split(".")[1]
	   			print(md+" "+topology+" Time=" + t)
				fwrite.write(md+" "+topology+" Time= " + str(t)+" (ns)"+"\n") 
			    	break
			line = fp.readline()
		fp.close()
fwrite.close()
				


    
            
