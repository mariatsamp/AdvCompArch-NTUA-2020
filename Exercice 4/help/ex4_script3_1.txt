#change the following paths:

SNIPER_EXE=/home/mary/advcomparch_ex4/sniper-7.3/run-sniper
SNIPER_CONFIG=/home/mary/advcomparch_ex4/help/ask4.cfg
OUTPUT_DIR_BASE=/home/mary/advcomparch_ex4/outputs
LOCKS_DIR=/home/mary/advcomparch_ex4/help/locks
MAKE_DIR=/home/mary/advcomparch_ex4/help/



declare -a modes=(TAS_CAS TAS_TS TTAS_CAS TTAS_TS MUTEX)

declare -a grainsizes=(1 10 100)


#USE ONLY ONE UN-COMMENTED comb PER EXECUTION!!!

#comb array has the form (ncores l2_shared_cores l3_shared_cores) 
#declare -a comb=(1 1 1)
#declare -a comb=(2 2 2)
declare -a comb=(4 4 4)
#declare -a comb=(8 4 8)
#declare -a comb=(16 1 8)

for MODE in "${modes[@]}";do

mkfile_mode="-D${MODE}"
sed_cmd="sed -i '8s/.*/LFLAG ?= ${mkfile_mode} /' ${MAKE_DIR}/Makefile"
/bin/bash -c "${sed_cmd}"
/bin/bash -c "make clean;"
/bin/bash -c "make;"


	for GRAINSIZE in "${grainsizes[@]}";do
		NCORES="${comb[0]}"
		NTHREADS="${comb[0]}"		
		L2_CORES="${comb[1]}"	
		L3_CORES="${comb[2]}"
		
			echo "-------------------------------"	
			echo "mode:${MODE}"	
			echo "number of threads:${NTHREADS}"
			echo "grainsize:${GRAINSIZE}"
			echo "number of cores:${NCORES}"		
			echo "L2 cores:${L2_CORES}"		
			echo "L3 cores:${L3_CORES}"		
			echo "-------------------------------"		
			echo

			COMB2_OUTDIR=$(printf "%d_threads/threads_%d_grainsize_%d" $NCORES $NTHREADS $GRAINSIZE)
			OUTDIR="${OUTPUT_DIR_BASE}/3_1/${MODE}/${COMB2_OUTDIR}"
			CMD="${SNIPER_EXE} -c ${SNIPER_CONFIG} -n $NCORES -d ${OUTDIR} --roi \
			-g --perf_model/l2_cache/shared_cores=$L2_CORES \
			-g --perf_model/l3_cache/shared_cores=$L3_CORES --\
			${LOCKS_DIR} $NTHREADS 1000 $GRAINSIZE"

			echo "${CMD}"
			/bin/bash -c "$CMD"
			#time ${CMD}
		
		
	done
done

