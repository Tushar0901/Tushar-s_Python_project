from apicem import *
try:
    resp= get(api="user")
    response_json = resp.json()
    print (json.dumps(response_json,indent=4),'\n')
except:
    print ("Something wrong with GET /user request")
    sys.exit()


for item in response_json["response"]:
    for item1 in item["authorization"]:
        print ("User \'%s\', role is the %s."%(item["username"],(item1["role"])[5:]))
