#!/usr/bin/python
import sys
import os
import time

jobs=5
job=0
while job < jobs: 
	for i in sys.argv[1:]:
		command="qsub mm.c.sge "+i+" mm_output_"+i+".out"
		os.system(command)
		time.sleep(5)
	job+=1
