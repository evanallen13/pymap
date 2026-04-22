import nmap

# Initialize the scanner
nm = nmap.PortScanner()
network=input("Print Network: ")

print(f"Pinging subnet {network}... please wait.")
nm.scan(hosts=network, arguments='-sn')
live_hosts = [h for h in nm.all_hosts() if nm[h].state() == 'up']
print(f"Found {len(live_hosts)} live host(s): {', '.join(live_hosts) if live_hosts else 'none'}")

print(f"\nScanning subnet {network}... please wait.")

# -F: Fast mode (scans fewer ports)
# --open: Only show hosts with at least one open port
nm.scan(hosts=network, arguments='-F --open')

# Iterate over all discovered hosts
for host in nm.all_hosts():
    print(f'\nHost : {host} ({nm[host].hostname()})')
    print(f'State : {nm[host].state()}')
    
    for proto in nm[host].all_protocols():
        print(f'Protocol : {proto}')
        ports = nm[host][proto].keys()
        for port in sorted(ports):
            print(f'port : {port}\tstate : {nm[host][proto][port]["state"]}')
