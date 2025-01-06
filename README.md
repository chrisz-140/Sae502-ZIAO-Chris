**Notice d’Utilisation : Simulation de Cyberattaques**

**1. Introduction**

Ce projet permet de déployer une plateforme de simulation de cyberattaques comprenant trois conteneurs Docker (« attaque », « victime », « logs ») orchestrés via Ansible. Le projet inclut des outils de scan et d’attaque (é.g., Nmap, Hydra) et une interface Python interactive pour exécuter des tests.

ATTENTION : la machine logs n’est pas fonctionnel donc on ne pourra que faire l’attaque.

-----
**2. Arborescence du Projet**

Voici la structure des fichiers et répertoires principaux :

projet-simulation-cyberattaques/

├── ansible

│   ├── ansible.cfg

│   ├── inventory

│   │   └── hosts

│   ├── playbooks

│   │   ├── deploy\_attaque.yml

│   │   ├── deploy\_logs.yml

│   │   ├── deploy\_victime.yml

│   │   └── site.yml

│   └── roles

│       ├── attaque

│       │   ├── tasks

│       │   │   └── main.yml

│       │   ├── templates

│       │   └── vars

│       │       └── main.yml

│       ├── logs

│       │   ├── tasks

│       │   │   └── main.yml

│       │   ├── templates

│       │   └── vars

│       │       └── main.yml

│       └── victime

│           ├── tasks

│           │   └── main.yml

│           ├── templates

│           └── vars

│               └── main.yml

├── docker

│   ├── docker-compose.yml

│   ├── Dockerfile\_attaque

│   ├── Dockerfile\_logs

│   └── Dockerfile\_victime

├── interface.py

├── README.md

├── requirements.yml

├── Sae502-ZIAO-Chris

│   └── README.md

├── scripts

│   └── setup\_network.sh

└── wordlist.txt
-----
**3. Étapes d'utilisation**

**Étape 1 : Vérifier l'environnement**

Avant de commencer, assurez-vous que :

- Docker est installé et fonctionne correctement sur votre machine.
- Ansible est installé et configuré.
- Vous êtes dans le répertoire racine de votre projet.

**Étape 2 : Construire les images Docker**

Dans votre projet, si vous avez des fichiers Dockerfile pour chaque conteneur, vous devez d'abord construire les images Docker. Utilisez les commandes suivantes :

cd docker
docker build -t docker\_attaque .

docker build -t docker\_victime .

docker build -t docker\_logs .

Ces commandes :

- Construisent les images Docker à partir des répertoires respectifs contenant les fichiers Dockerfile.
- Nomment les images docker\_attaque, docker\_victime, et docker\_logs.

**Étape 3 : Déployer avec Ansible**

Ansible est utilisé pour automatiser la configuration et le déploiement. Exécutez les commandes suivantes :

1. **Vérifiez que l'inventaire est correct :**

   Assurez-vous que votre fichier inventory/hosts contient les bonnes adresses IP ou noms de conteneurs.

1. **Lancez le playbook principal pour déployer les conteneurs :**

   cd ansible
   ansible-playbook -i inventory/hosts playbooks/site.yml

   Cette commande :

   1. Configure les conteneurs définis dans vos fichiers Ansible (par exemple, playbooks/deploy\_attaque.yml, playbooks/deploy\_victime.yml, etc.).
   1. Assure que tous les services nécessaires (comme SSH, Nmap, Hydra) sont installés et fonctionnels.

**Étape 4 : Démarrer manuellement les conteneurs (si nécessaire)**

Si Ansible n'est pas utilisé ou que vous voulez déployer manuellement, utilisez Docker Compose si un fichier docker-compose.yml est présent. Par exemple :

docker-compose up -d

Cette commande démarre tous les conteneurs définis dans docker-compose.yml en mode détaché.

**Étape 5 : Vérification**

1. **Listez les conteneurs en cours d'exécution :**

   docker ps

   Vous devriez voir vos conteneurs docker\_attaque, docker\_victime, et docker\_logs en cours d'exécution.

1. **Testez la connexion aux conteneurs via SSH :**

   ssh root@<container\_ip> -p <port>

1. **Vérifier les addresse ip des conteneurs**
-----
**Résumé des commandes**

|**Étape**|**Commande**|
| :-: | :-: |
|Construire les images|docker build -t docker\_attaque ./docker/attaque|
||docker build -t docker\_victime ./docker/victime|
||docker build -t docker\_logs ./docker/logs|
|Déployer avec Ansible|ansible-playbook -i inventory/hosts playbooks/site.yml|
|Déployer avec Docker Compose|docker-compose up -d|
|Vérifier les conteneurs|docker ps|
|Accéder via SSH|ssh root@<container\_ip> -p <port>|

-----
**4. Utilisation de l’interface Python**

1. **Accéder au fichier Python :** Chemin : scripts/interface.py
1. **Lancer le script :**

   python3 scripts/interface.py

1. **Options proposées par l’interface :**
   1. **Nmap :** Effectue un scan complet sur la cible.
   1. **Brute Force :** Lancement d'une attaque Hydra (attention cela ne sera pas realisable car je n’est pas fournis de wordlists).
1. **Exemple d’interaction avec l’utilisateur :**
   1. Entrer l’adresse IP de la victime.
   1. Choisir entre les options disponibles (« Nmap », « Brute Force » ou « Sortir »).
   1. ATTENTION : Uniquement l’option nmap fonctionne
-----
**5. Gestion des Erreurs**

**5.1 Erreur : Impossible de se connecter aux conteneurs via Ansible**

- **Message :** Invalid/incorrect password
- **Solution :**
  - Vérifier que les identifiants dans le fichier d’inventaire sont corrects.
  - Ajouter la ligne suivante dans ansible.cfg :
  - [defaults]

    host\_key\_checking = False

**5.2 Erreur : Python manquant dans les conteneurs**

- **Message :** /usr/bin/python: not found
- **Solution :**
  - Ajouter l’installation de Python dans les Dockerfiles des conteneurs.
  - Mettre à jour l’inventaire Ansible :

    ansible\_python\_interpreter=/usr/bin/python3

**5.3 Erreur : Problème lors du push Git**

- **Message :** Updates were rejected because the remote contains work that you do not have locally.
- **Solution :**
  - Synchroniser les modifications avec git pull origin main --rebase.
  - Ensuite, effectuer le push :

    git push origin main

**5.4 Erreur : Le scan Nmap ne retourne rien**

- **Cause probable :** La cible n’est pas en ligne.
- **Solution :**
  - Vérifier que le conteneur cible (« victime ») est démarré.
  - Utiliser la commande suivante pour tester la connectivité :

    ping <IP\_CIBLE>

**5.5 Problème avec Hydra dans l’interface Python**

- **Cause probable :** Mauvais chemin de wordlist ou mauvais port.
- **Solution :**
  - S’assurer que la wordlist existe au chemin fourni.
  - Vérifier que le port fourni est ouvert sur la cible avec Nmap.
-----
**6. Récapitulatif des Commandes Clés**

- **Déploiement des conteneurs :**

  ansible-playbook -i inventory/hosts playbooks/site.yml

- **Lancer l’interface Python :**

  python3 scripts/interface.py

- **Exécuter un scan Nmap via Docker pour tester si l’attaque fonctionne sans le code python :**

  docker exec attaque nmap -p- <IP\_CIBLE>

-----
Avec cette notice, vous avez tout le nécessaire pour utiliser et gérer le projet. En cas de problème, référez-vous aux solutions de la section « Gestion des Erreurs ».

