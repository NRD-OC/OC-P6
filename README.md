# OC-P6
Projet 6 de la formation AIC de OpenClassrooms

Ce programme vise à automatiser l'installation d'un serveur web Apache sur un serveur Linux Ubuntu.
Il a été testé avec succès sur Ubuntu Server 20.04 LTS. 
Il devrait également fonctionner (mais n'a pas été testé) sur un serveur Debian.

Le fichier du programme est "install_apache.py".
Dans la mesure où le programme modifie le système, il doit être exécuté en root (via un sudo sous Ubuntu).

Par exemple :

$ sudo python3 install_apache.py https://mon_site_web.local

Le programme effectue les actions suivantes :
- Indication de l'utilisation correcte en cas d'arguments invalides
- Mise à jour du système
- Install du paquet Apache
- Création du fichier de configuration du site web
- Création de la page d'accueil du site web
- Dans le cas d'un site en https, ajout du support SSL & création d'un certificat auto-signé
- Activation du site & désactivation du site par défaut d'Apache

Les autres fichiers n'ont pas d'utilité propre. Ils m'ont servi à tester certaines fonctionnalités, 
ce sont en quelque sorte les "briques" avec lequel j'ai contruit le programme principal.
Je les ai incluses afin d'expliciter l'écriture du programme.
