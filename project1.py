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
    
def avg_body_mass_by_species_and_sex(data):
    results = {}
    for row in data:
        species = row.get("species", "")
        sex = row.get("sex", "")
        body_mass = safe_float(row.get("body_mass_g", ""))
        if not species or not sex or body_mass is None:
            continue
        key = (species, sex)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += body_mass
        results[key]["count"] += 1
    avg = {f"{sp} ({sx})": round(v["total"] / v["count"], 2)
           for (sp, sx), v in results.items()}
    return avg

