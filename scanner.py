#!/bin/python3

import socket
import sys
from datetime import datetime

#Define our target
if len(sys.argv) == 3 : 
	#this is the host "target"
	target = socket.gethostbyname(sys.argv[1])

	#Define the port : 
	port_arg = str(sys.argv[2])
	port_list = port_arg.split("-") #Port will save into a list saparated by "-"
	from_port = int(port_list[0])
	to_port = int(port_list[1])


	#if there is not any argument or more argument

	#Adding a banner
	print("=" *50)
	print("Port scanner By \"RABIUS SANY\"")
	print("=" *50)
	print("Scanning host : ", sys.argv[1])
	print("Port range    : ", from_port, "to", to_port)
	print("Started       : ", datetime.now())
	print("=" *50)

	try:
		for port in range(from_port,to_port) : 
			# Now we will scan the host and put the connection into result variable.
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result == 0 :
				print("[OK] Open port : {}".format(port))
			s.close()
	except KeyboardInterrupt:
		
		print("\n[X] Exiting program.")
		sys.exit()
		

	except socket.gaierror : 
		
		print("[!] Hostname could not be resolved.")
		sys.exit()
		
	except socket.error : 
		
		print("[X] Could not connect to server.")
		sys.exit()
	print("-"*50)
	print("All port scan done")
	print("Developed By RABIUS SANY.")
	print("-"*50)
	
	
	
else : 
	print("=" * 50)
	print("Invalid amount of arguments")
	print("Syntex : python3 {} <IP> <port-port>".format(sys.argv[0]))
	print("Example : python3 {} 192.168.56.102 1-1000".format(sys.argv[0]))
	print("=" * 50)
