import subprocess

def main():
    print("=== Cyberattack Simulation ===")
    print("1 - Brute Force (Hydra)")
    print("2 - Port Scan (Nmap)")
    choice = input("Choose an attack [1-2]: ")

    if choice == "1":
        ip = input("Enter target IP: ")
        port = input("Enter port: ")
        wordlist = input("Enter path to wordlist: ")
        playbook = "brute_force.yml"
        command = f"ansible-playbook {playbook} -e target_ip={ip} -e target_port={port} -e wordlist={wordlist}"
        subprocess.run(command, shell=True)

    elif choice == "2":
        ip = input("Enter target IP: ")
        playbook = "ansible/port_scan.yml"
        command = f"ansible-playbook {playbook} -e target_ip={ip}"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    main()
