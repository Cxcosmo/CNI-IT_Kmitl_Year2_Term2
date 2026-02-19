from netmiko import ConnectHandler

router = {"device_type": "cisco_ios",
          "host": "172.16.3.2",
          "username": "admin",
          "password": "cisco"}

ip_List = [
            # {"source": "192.168.3.1", "destination": "192.168.3.129", "who":"My Router"},
            # {"source": "192.168.3.65", "destination": "192.168.3.129", "who":"My Router"},
            {"source": "192.168.3.1", "destination": "192.168.5.129", "who":"Other"},
            {"source": "192.168.3.65", "destination": "192.168.5.129", "who":"Other"}
        ]

connection = ConnectHandler(**router)

for ip in ip_List:
    source = ip["source"]
    destination_ip = ip["destination"]
    who = ip["who"]
    print(f"{source} -> {destination_ip} ({who})")
    output = connection.send_command(
        f"traceroute {destination_ip} source {source}",
        expect_string=r"#",
        read_timeout=60
    )

    print(output)

connection.disconnect()
