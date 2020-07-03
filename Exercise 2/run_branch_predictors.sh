#!/bin/bash

## Execute this script in the helpcode directory.
## Example of usage: ./run_branch_predictors.sh 403.gcc
## Modify the following paths appropriately
## CAUTION: use only absolute paths below!!!
PIN_EXE=/path/to/pin-3.2-81205-gcc-linux/pin
PIN_TOOL=/path/to/pintool/obj-intel64/cslab_branch.so
outDir="/path/to/outputs-dir"

for BENCH in $@; do
	cd spec_execs_train_inputs/$BENCH

	line=$(cat speccmds.cmd)
	stdout_file=$(echo $line | cut -d' ' -f2)
	stderr_file=$(echo $line | cut -d' ' -f4)
	cmd=$(echo $line | cut -d' ' -f5-)

	pinOutFile="$outDir/${BENCH}.cslab_branch_predictors.out"
	pin_cmd="$PIN_EXE -t $PIN_TOOL -o $pinOutFile -- $cmd 1> $stdout_file 2> $stderr_file"
	echo "PIN_CMD: $pin_cmd"
	/bin/bash -c "time $pin_cmd"

	cd ../../
done
