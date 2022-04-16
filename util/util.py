from client import ArkClient
from pathlib import Path


class Util:
    def __init__(self):
        pass
        
        
    def get_client(self, api_port, ip="localhost"):
        return ArkClient('http://{0}:{1}/api'.format(ip, api_port))
