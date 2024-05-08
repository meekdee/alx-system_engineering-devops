#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import json
import requests
import sys

def number_of_subscribers(subreddit):

    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
