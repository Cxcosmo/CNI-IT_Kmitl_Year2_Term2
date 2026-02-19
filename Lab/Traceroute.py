from netmiko import ConnectHandler

router = {"device_type": "cisco_ios",
          "host": "172.16.3.2",
          "username": "admin",
          "password": "cisco"}

destination_ip = "192.168.3.129"
source_list = ["192.168.3.1", "192.168.3.65"]

connection = ConnectHandler(**router)

for source in source_list:
    print(f"{source} -> {destination_ip}")
    output = connection.send_command(
        f"traceroute {destination_ip} source {source}",
        expect_string=r"#",
        read_timeout=60
    )

    print(output)

connection.disconnect()
