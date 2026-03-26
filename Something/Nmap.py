import subprocess

ip = "10.30.6.0/24"
result = subprocess.run(["nmap", "-sn", ip], capture_output=True, text=True)
lines = result.stdout.splitlines()

print("Nmap Result:")
for line in lines:
    if "Nmap scan report for" in line:
        print(line)