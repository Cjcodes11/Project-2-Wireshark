ip_addresses = ["192.168.1.1", "192.168.0.1", "192.168.0.255",]
ports = ["80", "443", "8080", "22", "21", "3389"]

while True:
    print('\n')
    scan = input("Type p for port scan or i for ip scan: ")
    print('\n')
    
    if scan == "i":

        for IP in ip_addresses:
            if IP == "192.168.1.1":
                print(f"Warning! {IP} needs to be configured.")
            else:
                print(f"{IP} is safe and secure")
    elif scan == "p":
        print("\n")
        for p in ports:
        
                    if p == "22":
                        print(f"Warning! {p} is an open port.")
                    else:
                        print(f"{p} is safe and closed port. Examine this port now")
    else:
         print("Invalid Input")
         break
    
            