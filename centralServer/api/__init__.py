from centralServer.api.sendtask import sendtask
# from centralServer.api.register import set_up
from centralServer.api.register import *
from centralServer.api.getInstanceData import *

import socket

local_ip = socket.gethostbyname(socket.gethostname())
values = {
    "name": "gaole",
    "ip": local_ip
}
print("start")
req = urllib.request.Request("https://mboard-middle-server.herokuapp.com/api/sendip", json.dumps(values).encode(encoding='UTF8'), headers={'Content-type':'application/json', 'Accept':'text/plain'})
response = urlopen(req)
print(response.read())
