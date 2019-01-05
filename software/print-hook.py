#!/usr/bin/env python

import os
import sys
import cups
import time
import tempfile

from subprocess import call

new_file, output_file = tempfile.mkstemp(dir="/dev/shm/", suffix=".jpg", prefix="print-hook")



#output_file = "/dev/shm/print-tile.jpg"

np = len(sys.argv) -1

if np < 1:
    print 'Not enough arguments'
    quit()


if np == 4:

    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"2460x1846+20+20", output_file])
    call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"2460x1846+20+20", "-texture", "printer-background.jpg", output_file])
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = printers.keys()[0]
    printer_name = "Canon_CP1000"
    cups.setUser('pi')

    print printer_name

    print_id = conn.printFile(printer_name, output_file, "Photo Booth", {})
    # Wait until the job finishes
    counter=1
    waiter=True
    while waiter:
	    counter+=1
		
		if conn.getJobs().get(print_id, None):
		    waiter = False
			
		if counter > 10:
		    waiter = False
			
		time.sleep(10)	
    
    time.sleep(10)
    os.unlink(output_file)









