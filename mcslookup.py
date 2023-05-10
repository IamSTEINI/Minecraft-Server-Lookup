import requests
import os
import socket

name = input("SERVERIP> ")
print("\nChecking "+name+"...")
response = requests.get('https://api.mcsrvstat.us/2/'+name)
if(response): os.system("cls")
status = response.json()
protocol = "Unknown"
hostname = "Unknown"
icon = "Unknown"
software = "Unknown"
version = "Unknown"
online = "Unknown"
ip = "Unknown"
port = "Unknown"
ping = "Unknown"
query = "Unknown"
srv = "Unknown"
querymismatch = "Unknown"
ipinsrv = "Unknown"
cnameinsrv = "Unknown"
animatedmotd = "Unknown"
cachetime = "Unknown"
cacheexpire = "Unknown"
apiversion = "Unknown"
rawmotd = "Unknown"
cleanmotd ="Unknown"
htmlmotd = "Unknown"
onlineplayers = "Unknown"
maxplayers = "Unknown"

try:
    ip = socket.gethostbyname(name)
    protocol = status['protocol']
    hostname = status['hostname']
    icon = status['icon']
    software = status['software']
    version = status['version']
    online = status['online']
    ip = status['ip']
    port = status['port']
    ping = status['debug']["ping"]
    query = status['debug']["query"]
    srv = status['debug']["srv"]
    querymismatch = status['debug']["querymismatch"]
    ipinsrv = status['debug']["ipinsrv"]
    cnameinsrv = status['debug']["cnameinsrv"]
    animatedmotd = status['debug']["animatedmotd"]
    cachetime = status['debug']["cachetime"]
    cacheexpire = status['debug']["cacheexpire"]
    apiversion = status['debug']["apiversion"]
    rawmotd = status['motd']["raw"]
    cleanmotd = status['motd']["clean"]
    htmlmotd = status['motd']["html"]
    onlineplayers = status['players']["online"]
    maxplayers = status['players']["max"]
    htmlmotd = str("".join(htmlmotd)).replace("\u2726", "").replace("   ", "")
except Exception:
    pass
if(onlineplayers != "Unknown" or maxplayers != "Unknown"):
    if(int(maxplayers) == int(onlineplayers) + 1):
        maxplayers = str(maxplayers) + " (Probably more, this is a method to get more players)"
htmlstring = f"""<!DOCTYPE html>
<html lang="en" style="background: black;">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="icon" type="image/png" href="{str(icon)}">
<title>INFO {hostname.replace("java.", "")}</title>
</head>
<body style="color:white;"><pre>
<h1>({hostname.replace("java.", "")})  Server Status Information:</h1>
<p style="font-size:18px;padding-left:10px;margin:auto;">`Unknown` means no informations.</p><br>
<p style="font-size:18px;padding-left:10px;margin:auto;">Protocol: {protocol}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Hostname: {hostname}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Software: {software}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Version: {version}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Online: {online}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">IP: {ip}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Query: {query}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Srv: {srv}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Query Mismatch: {querymismatch}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">IP in SRV: {ipinsrv}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Cname in SRV: {cnameinsrv}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Animated MOTD: {animatedmotd}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Cache Time: {cachetime}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Cache Expire: {cacheexpire}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">API Version: {apiversion}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">HTML MOTD: {htmlmotd}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Online Players: {onlineplayers}</p>
<p style="font-size:18px;padding-left:10px;margin:auto;">Max Players: {maxplayers}</p>
</pre>
<br>
"""+"""<style>
::-webkit-scrollbar {
    width: 0.2em;
    background-color: transparent;
}

::-webkit-scrollbar-thumb {
    background-color:transparent;
}

/* Firefox-Browser */
::-moz-scrollbar {
    width: 0.2em;
    background-color:transparent;
}

::-moz-scrollbar-thumb {
    background-color: transparent;
}

/* Internet Explorer-Browser */
::-ms-scrollbar {
    width: 0.2em;
    background-color: transparent;
}

::-ms-scrollbar-thumb {
    background-color: transparent;
}

</style>
"""+f"""
<img src="https://api.mcstatus.io/v2/widget/java/{name}?dark=true" style="border: none;bottom: opx;width: 700px;width: 30%;position: absolute;height: 16%;">
</body>
</html>"""
with open("server.html", "w") as f:
    f.writelines(str(htmlstring))
os.system("start server.html")