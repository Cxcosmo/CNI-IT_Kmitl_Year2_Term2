from netmiko import ConnectHandler

def main():
    print("HELLO! WELCOME TO THE ROUTER INFORMATION SCRIPT!")
    print("Please Select the Router you want to connect to:")
    print("1. My Router [172.16.3.1, 172.16.3.5, 172.16.3.9]")
    print("2. Custom Router")
    choice = input("Enter your choice (1 or 2): ")
    if choice == "1":
        routers = [
            {"device_type": "cisco_ios", "host": "172.16.3.1", "username": "admin", "password": "cisco"},
            {"device_type": "cisco_ios", "host": "172.16.3.5", "username": "admin", "password": "cisco"},
            {"device_type": "cisco_ios", "host": "172.16.3.9", "username": "admin", "password": "cisco"}
        ]

    elif choice == "2":
        device_type = input("Enter device type (e.g., cisco_ios): ")
        host = input("Enter router IP address: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        routers = [{"device_type": device_type, "host": host, "username": username, "password": password}]

    print("Select the information you want to retrieve:")
    print("1. Router Name")
    print("2. Router Specification")
    print("3. Router Interface")
    print("4. Routing Table")
    info_choice = input("Multi Select (e.g., 1 2 3): ").split()

    for router in routers:
        connection = ConnectHandler(**router)

        print("=================================")
        print("Router:", router["host"])
        print("=================================")

        for choice in info_choice:
            match choice:
                case "1":
                    print("----- Router Name -----")
                    print(connection.send_command("show running-config | include hostname"))
                case "2":
                    print("----- Router Specification -----")
                    print(connection.send_command("show version"))
                case "3":
                    print("----- Router Interface -----")
                    print(connection.send_command("show ip interface brief"))
                case "4":
                    print("----- Routing Table -----")
                    print(connection.send_command("show ip route"))

        connection.disconnect()


if __name__ == "__main__":    main()