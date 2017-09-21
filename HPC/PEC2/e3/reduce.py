#!/usr/bin/python
import sys
import os
import time

jobs=100
job=0
while job < jobs: 
	for i in sys.argv[1:]:
		command="qsub reduce_serial.sge "+i+" reduce_serial_output_"+i+".out"
		os.system(command)
		time.sleep(1)
		command="qsub reduce_openmp.sge "+i+" reduce_openmp_output_"+i+".out"
		os.system(command)
		time.sleep(5)
	job+=1
