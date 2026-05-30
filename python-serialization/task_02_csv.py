#!/usr/bin/python3
"""
Module for converting CSV data to JSON.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts CSV file to JSON file (data.json).
    Returns True if successful, False otherwise.
    """
    try:
        data = []

        with open(csv_filename, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)

        return True

    except Exception:
        return False
