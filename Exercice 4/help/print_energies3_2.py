import sys, os

energy_path = "/home/mary/advcomparch_ex4/mcpat_outputs/3_2"


fwrite = open("/home/mary/advcomparch_ex4/outputs/energies3_2.txt", "w")
modes = ["TAS_CAS", "TAS_TS", "TTAS_CAS","TTAS_TS","MUTEX"]
topologies = ["share-all","share-L3","share-nothing"]

for md in modes:
	for t in topologies:
		
		pathfile = energy_path+"/"+t+"/"+md+"/energy.total"
		fp = open(pathfile,'r')
		line = fp.readline()
		while line:
			if line.startswith("  total"):
				tokens = line.split()
	    			energy = float(tokens[3])
				if tokens[4] == "kJ":
						energy *= 1000;
	    			#bench = file.split("/")[6].split(".")[1]
	   			print(md+" "+t+" Energy=" + str(energy))
				fwrite.write(md+" "+t+" Energy=" + str(energy)+"\n") 
			    	break
			line = fp.readline()
		fp.close()
fwrite.close()
				


    
            
