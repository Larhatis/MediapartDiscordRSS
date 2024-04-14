Mediaprout - Script Python pour récupérer les articles d'un flux RSS et les publier sur Discord

Installation
Pour utiliser ce script, vous devez avoir Python 3 installé sur votre système. Ensuite, vous pouvez installer les bibliothèques nécessaires en utilisant pip :

pip install requests feedparser


Usage

Pour utiliser ce script, remplacez l'URL du flux RSS et l'URL du webhook Discord dans le code, puis exécutez le script Python. Le script récupérera les articles du flux RSS, publiera les nouveaux articles sur le channel Discord spécifié, et enregistrera la liste des articles déjà postés dans un fichier.

Par défaut, le script enregistre la liste des articles déjà postés dans un fichier nommé fichierMediaprout.rss dans le répertoire courant. Si le fichier n'existe pas, le script le créera automatiquement.

Dépendances

Ce script nécessite les bibliothèques Python suivantes :

requests : pour envoyer des requêtes HTTP à l'API Discord.
feedparser : pour parser les flux RSS.