import json
import time
from geoip import geolite2
from datetime import datetime, timedelta
#log file location is /var/log/iptables.log
log = '/var/log/iptables.log'

#Lists to keep track of connections
connectionsin = []
connectionsout = []

class connection(object):
	def __init__(self,dat,ip,tos,prec,ttl,prot,spt,dpt,leng):
		self.dat = dat
		self.ip = ip
		self.tos = tos
		self.prec = prec
		self.ttl = ttl
		self.prot = prot
		self.spt = spt
		self.dpt = dpt
		self.leng = leng

#just prints where in memory the objects are stored
def printConnections():
	print("INCOMING\n")
	for connection in connectionsin:
		print(connection)
	print("OUTGOING\n")
	for connection in connectionsout:
		print(connection)

def makeJson():
	with open('test.t', 'w') as f:
		json = "{\n\t\"name\": \"router\",\n\t\"children\": [{\n\t\"name\": \"162.243.75.48\",\n\t\"children\":[{\n\"name\":\"incoming\",\n\"children\":\n["
		for connection in connectionsin:
			json += "{\n\t\"date\": \""
			json += connection.dat
			json += "\",\n\t\"name\": \""
			json += connection.ip
			json += "\",\n\t\"geo\":\""
			match = geolite2.lookup(connection.ip)
			if match is not None:
				json+=match.country 
			json += "\",\n\t\"tos\": \""
			json += connection.tos
			json += "\",\n\t\"prec\": \""
			json += connection.prec
			json += "\",\n\t\"ttl\": \""
			json += connection.ttl
			json += "\",\n\t\"protocol\": \""
			json += connection.prot
			json += "\",\n\t\"spt\": \""
			json += connection.spt
			json += "\",\n\t\"dpt\": \""
			json += connection.dpt
			json += "\",\n\t\"size\": "
			json += connection.leng
			json += "},"
			#print(json)
		json = json[:-1]
		json +="]\n},{\"name\":\"outgoing\",\n\"children\":["
                for connection in connectionsout:
                        json += "{\n\t\"date\": \""
                        json += connection.dat
                        json += "\",\n\t\"name\": \""
                        json += connection.ip
			json += "\",\n\t\"geo\":\""
                        match = geolite2.lookup(connection.ip)
                        if match is not None:
                                json+=match.country
                        json += "\",\n\t\"tos\": \""
                        json += connection.tos
                        json += "\",\n\t\"prec\": \""
                        json += connection.prec
                        json += "\",\n\t\"ttl\": \""
                        json += connection.ttl
                        json += "\",\n\t\"protocol\": \""
                        json += connection.prot
                        json += "\",\n\t\"spt\": \""
                        json += connection.spt
                        json += "\",\n\t\"dpt\": \""
                        json += connection.dpt
                        json += "\",\n\t\"size\": "
                        json += connection.leng
                        json += "},"
                        #print(json)
		json = json[:-1]
		json+="]\n}]\n}]\n}"
		f.write(json)
		f.close()
		#HERE IS FINISHED JSON PRINT TO FILE
		#print(json)
		json_data = open("Data.json","w")
		json_data.write(json)
		json_data.close()

def combineDups():	
	testConnect = list(connectionsin)
	del connectionsin[:]
	for connection in testConnect:
		#print("here1")
		flag = False
		testIP = connection.ip
		testPort = connection.dpt
		#if not connectionsin:
		for dup_connection in connectionsin:
			#print("here")
			dupIP = dup_connection.ip
			dupPort = dup_connection.dpt
			if testIP == dupIP and testPort == dupPort:
				#print("dup")
 				flag = True
		if flag == False:
			connectionsin.append(connection)
	del testConnect [:]
	testConnect = list(connectionsout)
        del connectionsout[:]
        for connection in testConnect:
                flag = False
                testIP = connection.ip
                testPort = connection.spt
		#if not connectionsout:
		for dup_connection in connectionsout:
                       	dupIP =	dup_connection.ip
                       	dupPort = connection.spt
			if testIP == dupIP and testPort == dupPort:
                               	flag = True
                if flag	== False:
                        connectionsout.append(connection)

def deleteOld():
	now = datetime.now() - timedelta(minutes=10)
	#print(now)
	#fdate = datetime.strptime(connection.dat, '%b %d %H:%M:%S')
	#print(fdate)	
#var = 0
	testConnect = list(connectionsin)
	for connection in testConnect:
		fdate = datetime.strptime(connection.dat, '%b %d %Y %H:%M:%S')
		#print(now)
		#print(fdate)
		if fdate < now:	
			connectionsin.remove(connection)
	testConnect = list(connectionsout)
	for connection in testConnect:
		fdate = datetime.strptime(connection.dat, '%b %d %Y %H:%M:%S')
                if fdate < now:
                	connectionsout.remove(connection)

def parselog():
	#print("parsing\n")
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
					date = o[0] + ' ' + o[1] + ' 2016 ' + o[2]
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
					date = o[0] + ' ' + o[2] + ' 2016 ' + o[3]
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
					date = i[0] + ' ' + i[1] + ' 2016 ' + i[2]
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
					date = i[0] + ' ' + i[2] + ' 2016 ' + i[3]
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
			#connection = "root:router" + " host:" + host + " eth:" + eth + " ip:" + ip + " date:" + date + " tos:" + tos + " prec:" + prec + " ttl:" + ttl +  " protocol:" + protocol + " spt:" + spt + " dpt:" + dpt + " length:" + length
			#print(connection)
         
			#fdate = datetime.strptime(date, '%b %d %H:%M:%S') 
			if 'in' in eth:
				connectionsin.append(connection(date, ip, tos, prec, ttl, protocol, spt, dpt, length))
			elif "out" is eth:
				connectionsout.append(connection(date, ip ,tos, prec, ttl, protocol, spt, dpt, length))

#####
# Main
def main():
	while True:
		time.sleep(5)		
		parselog()
		#printConnections()
		deleteOld()
		combineDups()
		makeJson()
		open('/var/log/iptables.log','w').close()

main()