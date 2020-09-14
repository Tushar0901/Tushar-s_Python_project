#!/usr/bin/python

"""
This script returns all hosts and network devices in a tabular list.
"""

from apicem import * 
from scapy.all import *
import random

ip_list=[]
def get_host_and_device():
    """
    This function returns a list of all hosts and network devices with a number tag.
    """
    global ip_list
    idx=0
    try:
        resp= get(api="host")
        print ("Status of GET /host: ",resp.status_code)
        response_json = resp.json()
        if response_json["response"] !=[]:
            i=0
            for item in response_json["response"]:
                i+=1
                ip_list.append([i,"host",item["hostIp"]])
            idx=i
    except:
        print ("Something wrong, cannot get host IP list")
    try:
        resp= get(api="network-device")
        print ("Status: of GET /network-device ",resp.status_code)
        response_json = resp.json()
        if response_json["response"] !=[]:
            for item in response_json["response"]:
                idx+=1
                ip_list.append([idx,"network device",item["managementIpAddress"]])
#                print(ip_list)
    except:
        print ("Something wrong ! Cannot get network-device IP list !")
 

    if ip_list !=[]:
        return ip_list
    else:
        print ("There is no host or network device !")
        sys.exit()

if __name__ == "__main__":
    print (tabulate(get_host_and_device(),headers=['number','type','ip'],tablefmt="rst"))


"""
Now we will trceroute a destination ip address"
"""

#def get_hostname(ip_list):
 #   for a in ip_list:
#print(ip_list)
  #      hostname=a[2]
   # return hostname 
#print(hostname)
#get_hostname(ip_list)
for i in range(1, 28):
    pkt = IP(dst="218.1.100.100", ttl=i) / UDP(dport=33434)
    # Sending a packet, checking its reply
    reply = sr1(pkt, verbose=0)
    if reply is None:
        break
    elif reply.type == 3:
        # Final destnation
        print ("Done!"), reply.src
        break
    else:
        # Almost there
        print "%d hops away: " % i , reply.src
#        break
# Now scanning ports and checking if they are up or not
srcport = RandShort()

SYNACKpkt = sr1(IP(dst=target) /
                TCP(sport=srcport, dport=port, flags="S"))


pktflags = SYNACKpkt.getlayer(TCP).flags

if pktflags == SYNACK:
    pass
# ort is open
else:
    pass
