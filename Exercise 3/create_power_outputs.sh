#BENCHMARKS="astar cactusADM gcc GemsFDTD gobmk hmmer mcf omnetpp sjeng soplex xalancbmk zeusmp"

BENCHMARKS="gcc"
OUTPUTS="/home/mary/outputs/gcc/"
WINDOW="DW_01-WS_016.out DW_01-WS_032.out DW_01-WS_064.out DW_01-WS_096.out DW_01-WS_128.out DW_01-WS_192.out DW_01-WS_256.out DW_01-WS_384.out
		DW_02-WS_016.out DW_02-WS_032.out DW_02-WS_064.out DW_02-WS_096.out DW_02-WS_128.out DW_02-WS_192.out DW_02-WS_256.out DW_02-WS_384.out
		DW_04-WS_016.out DW_04-WS_032.out DW_04-WS_064.out DW_04-WS_096.out DW_04-WS_128.out DW_04-WS_192.out DW_04-WS_256.out DW_04-WS_384.out
		DW_08-WS_016.out DW_08-WS_032.out DW_08-WS_064.out DW_08-WS_096.out DW_08-WS_128.out DW_08-WS_192.out DW_08-WS_256.out DW_08-WS_384.out
		DW_16-WS_016.out DW_16-WS_032.out DW_16-WS_064.out DW_16-WS_096.out DW_16-WS_128.out DW_16-WS_192.out DW_16-WS_256.out DW_16-WS_384.out
		DW_32-WS_016.out DW_32-WS_032.out DW_32-WS_064.out DW_32-WS_096.out DW_32-WS_128.out DW_32-WS_192.out DW_32-WS_256.out DW_32-WS_384.out"

for bench in $BENCHMARKS; 
do
	for win in $WINDOW;
	do
		./advcomparch_mcpat.py -d $OUTPUTS/$bench/$bench.$win -t total -o $OUTPUTS/$bench/$bench.$win/power > $OUTPUTS/$bench/$bench.$win/power.total.out
	done
done
