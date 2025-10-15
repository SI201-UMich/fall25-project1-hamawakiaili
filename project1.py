import csv
import unittest

def load_data(filename):
    data = []
    with open(filename, "r", encoding="utf-8") as infile:
        csv_reader = csv.DictReader(infile)
        for row in csv_reader:
            data.append(row)
    return data

def safe_float(value):
    try:
        val = float(value)
        return val
    except (ValueError, TypeError):
        return None