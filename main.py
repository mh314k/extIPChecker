'''
External IP cheker
'''
from requests import get
import time

if __name__ == "__main__":
    ip_address = get('https://api.ipify.org').content.decode('utf8')
    print(ip_address)
    while(1):
        time.sleep(1)
        _ip = get('https://api.ipify.org').content.decode('utf8')
        if _ip != ip_address:
            ip_address = _ip
            print(ip_address)
