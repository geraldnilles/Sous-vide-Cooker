import socket
import struct
import json

UNIX_SOCKET_PATH = "/mnt/SousVideController"
TIMEOUT = 5
CHUNK_SIZE = 4096


# Receive a message
def recv(conn):
	pkt = ""
	while(1):
		pkt += s.recv(CHUNK_SIZE)
		msg,size = pkt_to_json(pkt)
		if msg != None:
			return msg
		# If msg is not none continue the loop

# Send a message
def send(msg,path = UNIX_SOCKET_PATH):
	s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	s.settimeout(TIMEOUT)

	pkt = json_to_pkt(msg)

	while(1):
		sent = s.send(pkt)
		if sent >= len(pkt):
			break
		else:
			pkt = pkt[sent:]
	
	return 0

## Convert IPC Packet to JSON object
#
# This function converts a n IPC packet into a JSON object.  The first 4 bytes
# contains the totle packet size.  
def pkt_to_json(pkt):
	# Grab the pkt length from the first 4 bytes
	if len(pkt) < 4:
		return (None, 0 )
	header = pkt[0:4]
	size = struct.unpack("<I",header)[0]

	# If the packet is shorter than the expected length, return None,0
	if len(pkt) < size+4:
		return (None,0 )

	# Convert the packet to JSON object
	payload = pkt[4:4+size]	
	obj = json.loads(payload)
	# Return how much of the string buffer was used
	return (obj,size+4)	

## Convert JSON object to an IPC packet
#
# Stringify's the JSON object and adds a 4byte unsigned interger to the 
# beginning of the packet to idenfiy the length
def json_to_pkt(obj):
	pkt = json.dumps(obj)

	header = struct.pack("<I",len(pkt))

	pkt = header+pkt
	return pkt


