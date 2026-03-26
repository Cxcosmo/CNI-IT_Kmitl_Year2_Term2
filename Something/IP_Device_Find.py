import subprocess

result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
lines = result.stdout.splitlines()

check = True

your_local_ip = ["192.168.113.1", "192.168.203.1"]
network_ip = []
ipv4_addresses = []
mac_addresses = []

for line in lines:
    if "Interface:" in line and any(ip in line for ip in your_local_ip):
        check = False
    if "Interface:" in line and not any(ip in line for ip in your_local_ip):
        check = True
        network_ip_set = (line.split()[1]).split(".")
        network_ip_set = network_ip_set[:-1]
        network_ip.append(".".join(network_ip_set))
    if check and "Internet Address" not in line and "Interface:" not in line and line.strip():
        parts = line.split()
        if len(parts) >= 2 and any(parts[0].startswith(ip) for ip in network_ip):
            ipv4_addresses.append(parts[0])
            mac_addresses.append(parts[1])

count_ip = len(ipv4_addresses)
print("Count IP:", count_ip)

for i in range(count_ip):
    print("--------------------------------")
    print("IPv4:", ipv4_addresses[i])
    print("MAC:", mac_addresses[i])
    result_traceroute = (subprocess.run(["tracert", "-h", "2", ipv4_addresses[i]], capture_output=True, text=True)).stdout.splitlines()
    print("Traceroute Result:")
    for line in result_traceroute:
        if ipv4_addresses[i] in line:
            print(line)
            detail = line.split()
            break
    for j in range(len(detail)):
        if ipv4_addresses[i] in detail[j]:
            print("Device Name:", detail[j-1])
            break
