from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "172.16.3.2",
    "username": "admin",
    "password": "cisco"
}

# ---------------- CONFIG SECTION ----------------

config_commands = [
    "no access-list 102",
    "no route-map PBR_R2",
    "access-list 102 permit ip 192.168.3.64 0.0.0.63 192.168.3.128 0.0.0.63",
    "route-map PBR_R2 permit 10",
    "match ip address 102",
    "set ip next-hop 172.16.3.1",
    "route-map PBR_R2 permit 20",
    "ip local policy route-map PBR_R2"
]

# ---------------- TRACEROUTE LIST ----------------

ip_List = [
    {"source": "192.168.3.1", "destination": "192.168.3.129", "who": "My Router"},
    {"source": "192.168.3.65", "destination": "192.168.3.129", "who": "My Router"},
    {"source": "192.168.3.1", "destination": "192.168.5.129", "who": "Other"},
    {"source": "192.168.3.65", "destination": "192.168.5.129", "who": "Other"}
]

# ---------------- EXECUTION ----------------

connection = ConnectHandler(**router)

print("=== Sending Configuration to R2 ===")
output = connection.send_config_set(config_commands)
print(output)

connection.save_config()

print("\n=== Testing Traceroute ===")

for ip in ip_List:
    source = ip["source"]
    destination = ip["destination"]
    who = ip["who"]

    print(f"\n{source} -> {destination} ({who})")

    output = connection.send_command(
        f"traceroute {destination} source {source}",
        expect_string=r"#",
        read_timeout=60
    )

    print(output)

connection.disconnect()
