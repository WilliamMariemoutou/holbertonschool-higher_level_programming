#!/usr/bin/python3
"""program to convert CSV to JSON using serializationa"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """converts the CSV file to JSON format and writes it into data.json"""
    try:
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]

            with open('data.json', mode='w') as json_file:
                json.dump(data, json_file, indent=4)

        return True

    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False

    except Exception as e:
        print(f"ErrorP: {e}")
        return False
