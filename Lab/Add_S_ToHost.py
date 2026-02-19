from netmiko import ConnectHandler

routers = [
    {"device_type": "cisco_ios", "host": "172.16.3.1", "username": "admin", "password": "cisco"},
    {"device_type": "cisco_ios", "host": "172.16.3.5", "username": "admin", "password": "cisco"},
    {"device_type": "cisco_ios", "host": "172.16.3.9", "username": "admin", "password": "cisco"}
]

for router in routers:
    connection = ConnectHandler(**router)

    name = ((connection.send_command("show running-config | include hostname")).split())[1]
    name = name.replace("s", "")

    connection.send_config_set(f"hostname {name + 's'}")
    connection.save_config()

    print(connection.send_command("show running-config | include hostname"))

    connection.disconnect()
