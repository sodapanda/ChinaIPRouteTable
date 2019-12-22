with open('china_ip_list.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

with open("add_route.sh", "a") as shellFile:
    for item in content:
        cmdLine = f"ip route add {item} via 192.168.50.1 dev eth0.2\n"
        shellFile.write(cmdLine)
