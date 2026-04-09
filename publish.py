import logging
import os
import sys
import xml.etree.ElementTree as ET

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("podcast")

PUBLISHED_FILE = './published_episodes.txt'


def fetch_last_episode(feed_url: str) -> dict:
    response = requests.get(feed_url)
    response.raise_for_status()

    root = ET.fromstring(response.content)
    item = root.find('./channel/item')

    if item is None:
        raise Exception("Nessun episodio trovato nel feed")

    title = item.findtext('title', '').strip()
    link = item.findtext('link', '').strip()

    if not title or not link:
        raise Exception(f"Titolo o link mancante nell'episodio: {title=} {link=}")

    return {'title': title, 'link': link}


def is_published(link: str) -> bool:
    if not os.path.exists(PUBLISHED_FILE):
        return False
    with open(PUBLISHED_FILE, 'r') as f:
        return link in f.read()


def mark_as_published(link: str) -> None:
    logger.info(f"Segnato come pubblicato: {link}")
    with open(PUBLISHED_FILE, 'a') as f:
        f.write(f"{link}\n")


def publish_to_linkedin(episode: dict, access_token: str, personal_urn: str, template: str) -> None:
    content = template.replace('{title}', episode['title']).replace('{link}', episode['link'])

    logger.info(f"Pubblicazione su LinkedIn: {content[:80]}...")

    post_data = {
        "author": f"urn:li:person:{personal_urn}",
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {"text": content},
                "shareMediaCategory": "ARTICLE",
                "media": [{"status": "READY", "originalUrl": episode['link']}]
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    response = requests.post(
        "https://api.linkedin.com/v2/ugcPosts",
        headers={
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json',
            'x-li-format': 'json'
        },
        json=post_data
    )

    if response.status_code != 201:
        raise Exception(f"Errore LinkedIn API {response.status_code}: {response.text}")

    logger.info("Post pubblicato con successo!")


if __name__ == "__main__":
    feed_url = os.environ['PODCAST_RSS_URL']
    access_token = os.environ['LINKEDIN_ACCESS_TOKEN']
    personal_urn = os.environ['LINKEDIN_PERSON_URN']
    template = os.environ['LINKEDIN_MESSAGE_TEMPLATE']

    episode = fetch_last_episode(feed_url)
    logger.info(f"Ultimo episodio: {episode['link']}")

    if is_published(episode['link']):
        logger.info("Episodio già pubblicato, niente da fare.")
        sys.exit(0)

    publish_to_linkedin(episode, access_token, personal_urn, template)
    mark_as_published(episode['link'])
