from apicem import * 


def get_host_and_device():

    ip_list=[]
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
    except:
        print ("Something wrong ! Cannot get network-device IP list !")

    if ip_list !=[]:
        return ip_list
    else:
        print ("There is no any host or network device !")
        sys.exit()

if __name__ == "__main__": 
    print (tabulate(get_host_and_device(),headers=['number','type','ip'],tablefmt="rst"))
