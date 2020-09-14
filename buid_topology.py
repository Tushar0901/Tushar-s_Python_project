import requests
import json

requests.packages.urllib3.disable_warnings()

controller='devnetapi.cisco.com/sandbox/apic_em'


def getTicket():
	url = "https://" + controller + "/api/v1/ticket"
	payload = {"username":"devnetuser","password":"Cisco123!"}	
	header = {"content-type": "application/json"}

	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
	print (response)

	r_json=response.json()

	ticket = r_json["response"]["serviceTicket"]

	return ticket


def getTopology(ticket):
	url = "https://" + controller + "/api/v1/topology/physical-topology"
	header = {"content-type": "application/json", "X-Auth-Token":ticket}
	response = requests.get(url, headers=header, verify=False)
	print ("Topology = ")
	print (json.dumps(response.json(), indent=4, separators=(',', ': ')))
	
	r_json=response.json()
	
	for n in r_json["response"]["nodes"]:		
	#	print()
	#	print()
		print('{:30}'.format("Node") + '{:25}'.format("Family") + '{:20}'.format("Label")+ "Management IP")
		if "platformId" in n:
			print('{:30}'.format(n["platformId"]) + '{:25}'.format(n["family"]) + '{:20.14}'.format(n["label"]) + n["ip"])
		else:
			print('{:30}'.format(n["role"]) + '{:25}'.format(n["family"]) + '{:20.14}'.format(n["label"]) + n["ip"])
		found=0    
		printed=0 
		for i in r_json["response"]["links"]:
			if i["source"] == n["id"]:
				if found==0:
					print('{:>20}'.format("Source Interface") + '{:>15}'.format("Target") +'{:>28}'.format("Target Interface") + '{:>15}'.format("Status") )
					found=1
					printed=1					
				for n1 in r_json["response"]["nodes"]:
					if i["target"] == n1["id"]:
						if "startPortName" in i:
							print("    " + '{:<25}'.format(i["startPortName"]) + '{:<18.14}'.format(n1["label"]) + '{:<25}'.format(i["endPortName"]) + '{:<9}'.format(i["linkStatus"]) )
						else:
							print("    " + '{:<25}'.format("unknown") + '{:<18.14}'.format(n1["label"]) + '{:<25}'.format("unknown") + '{:<9}'.format(i["linkStatus"]) )
						break;
		found=0				
		for i in r_json["response"]["links"]:
			if i["target"] == n["id"]:
				if found==0:
					if printed==1:
						print()
					print('{:>10}'.format("Source") + '{:>30}'.format("Source Interface") + '{:>25}'.format("Target Interface") + '{:>13}'.format("Status"))
					found=1					
				for n1 in r_json["response"]["nodes"]:
					if i["source"] == n1["id"]:
						if "startPortName" in i:							
							print("    " + '{:<20}'.format(n1["label"]) + '{:<25}'.format(i["startPortName"]) + '{:<23}'.format(i["endPortName"]) + '{:<8}'.format(i["linkStatus"]))
						else:
							print("    " + '{:<20}'.format(n1["label"]) + '{:<25}'.format("unknown") + '{:<23}'.format("unknown") + '{:<8}'.format(i["linkStatus"]))
						break;
		
theTicket=getTicket()
getTopology(theTicket)
