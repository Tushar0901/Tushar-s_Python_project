import requests
import json
from flask import Flask
from flask import render_template, jsonify
controller = 'devnetapi.cisco.com/sandbox/apic_em'


def getTicket():
    url = "https://" + controller + "/api/v1/ticket"
    payload = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    response = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
    print(response)
    r_json = response.json()
    ticket = r_json["response"]["serviceTicket"]
    return ticket

def getTopology(ticket):
    url = "https://" + controller + "/api/v1/topology/physical-topology"
    header = {"content-type": "application/json", "X-Auth-Token": ticket}
    response = requests.get(url, headers=header, verify=False)
    r_json = response.json()
    return r_json["response"]

app = Flask(__name__)
	
@app.route("/")
def index():
    return render_template("topology.html")

@app.route("/api/topology")
def topology():
    theTicket = getTicket()
    return jsonify(getTopology(theTicket))

if __name__ == "__main__":
    app.run()
