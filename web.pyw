import time
from datetime import datetime as dt
hosts_temp="E:\\Website Blocker\\hosts"
host_path = "C:\\Windows\\System32\\drivers\\etc\\hosts"
redirect="127.0.0.1"
websites=["www.facebook.com","facebook.com","google.com","www.google.com"]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,9):
        print("working hours...")
        with open(host_path,'r+') as file:
            content=file.read()
            for website in websites:
                if website in content:
                    pass
                else:
                  file.write(redirect+ " " +website+"\n")
    else:
        with open(host_path,'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()
        print("fun hours...")

    time.sleep(5)