#!/usr/bin/python3
"""
Module: task_02_requests
Fetches and processes posts from JSONPlaceholder API.
"""

import requests
import csv


def fetch_and_print_posts():
    """
    Fetch all posts and print their titles.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post.get("title"))


def fetch_and_save_posts():
    """
    Fetch posts and save them into a CSV file.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")

    if response.status_code == 200:
        posts = response.json()

        structured_posts = []

        for post in posts:
            structured_posts.append({
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)
