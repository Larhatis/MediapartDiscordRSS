import requests
import feedparser
import os
import json


def get_articles(feed_url): # Requête de flux RSS
    feed = feedparser.parse(feed_url)
    articles = [] # Liste des articles
    for entry in feed.entries:
        articles.append({ # Ajout des articles à la liste
            "title": entry.title,
            "link": entry.link
        })
    return articles

def post_to_discord(webhook_url, articles, posted_articles): # Publication dans un channel Discord
    new_articles = [article for article in articles if article['link'] not in posted_articles]
    for article in new_articles:
        data = {
            "content": f"**{article['title']}**\n{article['link']}"
        }
        response = requests.post(webhook_url, data=data)
        if response.status_code != 204:
            raise ValueError(f"Request to Discord returned an error {response.status_code}, the response is:\n{response.text}")
        else:
            posted_articles.add(article['link'])
    return posted_articles

def load_posted_articles(file_path): # Charge la liste des articles déjà postés à partir d'un fichier.
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return set(json.load(file))
    else:
        return set()

def save_posted_articles(file_path, posted_articles): #Enregistre la liste des articles déjà postés dans un fichier
    with open(file_path, 'w') as file:
        json.dump(list(posted_articles), file)

# Utilisez votre URL de flux RSS
feed_url = "https://www.mediapart.fr/articles/feed" #le flux rss de mediapart
articles = get_articles(feed_url)

# Remplacez ceci par votre URL de webhook Discord
webhook_url = "https://discord.com/api/webhooks/***************************************************Mettre votre webhook"

# Fichier pour stocker les articles déjà postés
file_path = "fichierMediaprout.rss" #fichier qui stocke les articles de mediapart déjà postés

posted_articles = load_posted_articles(file_path) # Charge la liste des articles déjà postés
posted_articles = post_to_discord(webhook_url, articles, posted_articles) # Publication des articles
save_posted_articles(file_path, posted_articles) 
