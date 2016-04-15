#!/bin/bash

#The script simply runs the tcpdummp command and stores the packets captured to
#a rotating file. The name of the file will be VFCaptureALL along with a timestamp
#in the format year:month:date. It listens on all interfaces and rotates every
#30 minutes.

DATE=`date +%Y:%m:%d`
FILE="VFCaptureAll_"$DATE".pcap"
#tcpdump -Z root -W 3 -C 3 -G 15 -w $FILE -i any #attempted to create circular window with this by having rotating files, but still overwrites single file. need to look more into this.
tcpdump -G 1800 -w $FILE -i any
