#location on server /usr/local/bin

#log file location is /var/log/iptables.log
log = '/var/log/iptables.log'
with open(log, 'r') as f:
   #read every line in file
   for line in f:
      #print(line)

      ###########################################################
      #
      #  VARIABLES
      #
      #  date - month (apr) day (1) time (13:00:01)
      #  host -  hostname of machine requesting a connection
      #  eth - whether connection is incoming of outgoing
      #  ip - this is the ip we are establishing a connection to
      #  tos - type of service of ip packet
      #  prec - precedence of the ip packet
      #  protocol - TCP, UDP, ICMP
      #  spt - source port
      #  dst - destination port
      #  length - length of packet header + payload
      #
      ############################################################

      #parse outgoing connections
      if "Outgoing" in line:
         o = line.split(" ")
         if o[1] is not "":
            #to fix weird bug when day is single digit.
            #bug is when single digit date, the log saves 2 \s characters
            #this must be accountd for in order to extract correct info at all times
            date = o[0] + " " + o[1] + " " + o[2]
            host = o[3]
            eth = "out"
            ip = o[11].lstrip('DST=')
            tos = o[13].lstrip('TOS=')
            prec = o[14].lstrip('PREC=')
            ttl = o[15].lstrip('TTL=')
            protocol = o[18]
            spt = o[19].lstrip('SPT=')
            dpt = o[20].lstrip('DPT=')
            if "LEN" in o[21]:
               length = o[21].lstrip('LEN=')
            else:
               length = o[12].lstrip('LEN=')
         else:
            date = o[0] + " " + o[2] + " " + o[3]
            host = o[4]
            eth = "out"
            ip = o[12].lstrip('DST=')
            tos = o[14].lstrip('TOS=')
            prec = o[15].lstrip('PREC=')
            ttl = o[16].lstrip('TTL=')
            protocol = o[19]
            spt = o[20].lstrip('SPT=')
            dpt = o[21].lstrip('DPT=')
            if "LEN" in o[22]:
               length = o[22].lstrip('LEN=')
            else:
               length = o[13].lstrip('LEN=')
      #parse incoming connections
      elif "Incoming" in line:
         i = line.split(" ")
         if i[1] is not "":
            date = i[0] + " " + i[1] + " " + i[2]
            host = i[3]
            eth = "in"
            ip = i[11].lstrip('SRC=')
            length = i[13].lstrip('LEN=')
            tos = i[14].lstrip('TOS=')
            prec = i[15].lstrip('PREC=')
            ttl = i[16].lstrip('TTL=')
            if "PROTO" not in i[18]:
               protocol = i[19]
               spt = i[20].lstrip('SPT=')
               dpt = i[21].lstrip('DPT=')
            else:
               protocol = i[18]
               spt = i[19].lstrip('SPT=')
               dpt = i[20].lstrip('DPT=')
         else:
            date = i[0] + " " + i[2] + " " + i[3]
            host = i[4]
            eth = "in"
            ip = i[12].lstrip('SRC=')
            length = i[14].lstrip('LEN=')
            tos = i[15].lstrip('TOS=')
            prec = i[16].lstrip('PREC=')
            ttl = i[17].lstrip('TTL=')
            if "PROTO" not in i[19]:
               protocol = i[20]
               spt = i[21].lstrip('SPT=')
               dpt = i[22].lstrip('DPT=')
            else:
               protocol = i[19]
               spt = i[20].lstrip('SPT=')
               dpt = i[21].lstrip('DPT=')
      #Can not use lstrip for protocol, must do a check
      if "TCP" in protocol:
         protocol = "TCP"
      elif "UDP" in protocol:
         protocol = "UDP"
      elif "ICMP" in protocol:
         protocol = "ICMP"
         #no port exists for ICMP
         spt = ""
         dpt = ""
         #typical ICMP packet size.  Should be fixed to get real size.
         length = "78"
      connection = "root:router" + " host:" + host + " eth:" + eth + " ip:" + ip + " date:" + date + " tos:" + tos + " prec:" + prec + " ttl:" + ttl +  " protocol:" + protocol + " spt:" + spt + " dpt:" + dpt + " length:" + length
      print(connection)