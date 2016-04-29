#!/bin/bash


#The script simply runs the tcpdummp command and stores the packets captured to
#a rotating file. The name of the file will be VFCaptureALL along with a timestamp
#in the format year:month:date:current file rotation. It listens on all interfaces
#and rotates every 5 minutes. It will make up to 10 files starting at 0.

DATE=`date +%Y:%m:%d`
FILE="VFCaptureAll_"$DATE

FCOUNTER=0

while :
do
    tcpdump -i any -c 100000 -G 300 -w ${FILE}:${FCOUNTER}.pcap
    FCOUNTER=${FCOUNTER+1}
    if [$FCOUNTER -ge 10];
    then
        FCOUNTER=0
    fi
done

#captures up to 100000 packets or changes files after 5 minutes
