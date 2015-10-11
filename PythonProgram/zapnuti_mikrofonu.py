#!/usr/bin/python
import time
import os
 
 os.system("/home/pi/use_case_scripts/Record_from_lineIn_Micbias.sh")
 sleep(1)
 #PO DOBU JEDNE SEKUNDY
 os.system("/home/pi/use_case_scripts/Reset_lineIn_Micbias.sh")
