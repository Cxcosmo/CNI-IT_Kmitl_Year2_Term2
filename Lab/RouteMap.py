from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "172.16.3.2",
    "username": "admin",
    "password": "cisco"
}

destination_ip = "192.168.3.129"
source_list = ["192.168.3.1", "192.168.3.65"]

config_commands = [
    "access-list 102 permit ip 192.168.3.64 0.0.0.63 192.168.3.128 0.0.0.63",
    "route-map PBR_R2 permit 10",
    "match ip address 102",
    "set ip next-hop 172.16.3.1",
    "route-map PBR_R2 permit 20",
    "ip local policy route-map PBR_R2"
]

connection = ConnectHandler(**router)

print("=== Sending Configuration to R2 ===")
output = connection.send_config_set(config_commands)
print(output)

connection.save_config()

print("\n=== Testing Traceroute ===")
for source in source_list:
    print(f"\n{source} -> {destination_ip}")
    output = connection.send_command(
        f"traceroute {destination_ip} source {source}",
        expect_string=r"#",
        read_timeout=60
    )
    print(output)

connection.disconnect()
