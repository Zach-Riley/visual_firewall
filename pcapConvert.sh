#!/bin/bash

#script to call on pcap2har code which converts HTTP packets in
#FILE into a .har file. FILE will be a pcap file which was obtained
#from the tcpdump command in capture.sh


FILE=$1


python ./pcap2har/main.py $FILE pcap.har
