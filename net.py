import socket

def port_scan(target, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    target = input("Enter target IP address or hostname: ")
    port_range = input("Enter port range (example 1-1000): ")
    start_port, end_port = map(int, port_range.split('-'))

    ports_to_scan = range(start_port, end_port + 1)

    print(f"Scanning ports {start_port}-{end_port} on {target}...")
    open_ports = port_scan(target, ports_to_scan)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")

