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

def avg_bill_length_by_island_and_year(data):
    results = {}
    for row in data:
        island = row.get("island", "")
        year = row.get("year", "")
        bill_length = safe_float(row.get("bill_length_mm", ""))
        if not island or not year or bill_length is None:
            continue
        key = (island, year)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += bill_length
        results[key]["count"] += 1
    avg = {f"{island} ({year})": round(v["total"] / v["count"], 2)
           for (island, year), v in results.items()}
    return avg

def avg_flipper_length_by_species_and_island(data):
    results = {}
    for row in data:
        species = row.get("species", "")
        island = row.get("island", "")
        flipper_length = safe_float(row.get("flipper_length_mm", ""))
        if not species or not island or flipper_length is None:
            continue
        key = (species, island)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += flipper_length
        results[key]["count"] += 1
    avg = {f"{sp} ({isle})": round(v["total"] / v["count"], 2)
           for (sp, isle), v in results.items()}
    return avg


def body_mass_difference_by_sex_and_island(data):
    temp = {}
    for row in data:
        sex = row.get("sex", "").upper()
        island = row.get("island", "")
        mass = safe_float(row.get("body_mass_g", ""))
        if not sex or not island or mass is None:
            continue
        key = (island, sex)
        if key not in temp:
            temp[key] = {"total": 0, "count": 0}
        temp[key]["total"] += mass
        temp[key]["count"] += 1

    results = {}
    for island in set(i for i, _ in temp.keys()):
        male_key = (island, "MALE")
        female_key = (island, "FEMALE")
        if male_key in temp and female_key in temp:
            male_avg = temp[male_key]["total"] / temp[male_key]["count"]
            female_avg = temp[female_key]["total"] / temp[female_key]["count"]
            results[island] = round(male_avg - female_avg, 2)
    return results

def bill_depth_vs_flipper_length_by_species(data):
    results = {}
    for row in data:
        species = row.get("species", "")
        bill_depth = safe_float(row.get("bill_depth_mm", ""))
        flipper_length = safe_float(row.get("flipper_length_mm", ""))
        if not species or bill_depth is None or flipper_length is None:
            continue
        if species not in results:
            results[species] = {"bill_total": 0, "flip_total": 0, "count": 0}
        results[species]["bill_total"] += bill_depth
        results[species]["flip_total"] += flipper_length
        results[species]["count"] += 1
    avg = {species: {
        "avg_bill_depth": round(v["bill_total"] / v["count"], 2),
        "avg_flipper_length": round(v["flip_total"] / v["count"], 2)
    } for species, v in results.items()}
    return avg

def avg_bill_length_by_year_and_sex(data):
    results = {}
    for row in data:
        year = row.get("year", "")
        sex = row.get("sex", "")
        bill_length = safe_float(row.get("bill_length_mm", ""))
        if not year or not sex or bill_length is None:
            continue
        key = (year, sex)
        if key not in results:
            results[key] = {"total": 0, "count": 0}
        results[key]["total"] += bill_length
        results[key]["count"] += 1
    avg = {f"{year} ({sex})": round(v["total"] / v["count"], 2)
           for (year, sex), v in results.items()}
    return avg

def main():
    filename = "penguins.csv"
    data = load_data(filename)

    results = {
        "Average Body Mass by Species and Sex": avg_body_mass_by_species_and_sex(data),
        "Average Bill Length by Island and Year": avg_bill_length_by_island_and_year(data),
        "Average Flipper Length by Species and Island": avg_flipper_length_by_species_and_island(data),
        "Body Mass Difference by Sex and Island": body_mass_difference_by_sex_and_island(data),
        "Bill Depth vs Flipper Length by Species": bill_depth_vs_flipper_length_by_species(data),
        "Average Bill Length by Year and Sex": avg_bill_length_by_year_and_sex(data)
    }

    with open("penguin_results_all.txt", "w", encoding="utf-8") as f:
        for title, result in results.items():
            f.write(f"{'='*60}\n")
            f.write(f"{title}\n")
            f.write(f"{'='*60}\n")
            for key, value in result.items():
                f.write(f"{key}: {value}\n")
            f.write("\n")

    print("✅ All results written to 'penguin_results_all.txt' successfully!")

class TestPenguinFunctions(unittest.TestCase):

    def setUp(self):
        self.sample_data = [
            {"species": "Adelie", "island": "Torgersen", "bill_length_mm": "39.1", "bill_depth_mm": "18.7",
             "flipper_length_mm": "181", "body_mass_g": "3750", "sex": "MALE", "year": "2007"},
            {"species": "Adelie", "island": "Torgersen", "bill_length_mm": "39.5", "bill_depth_mm": "17.4",
             "flipper_length_mm": "186", "body_mass_g": "3800", "sex": "FEMALE", "year": "2007"},
            {"species": "Gentoo", "island": "Biscoe", "bill_length_mm": "49.5", "bill_depth_mm": "15.9",
             "flipper_length_mm": "222", "body_mass_g": "5250", "sex": "FEMALE", "year": "2009"},
            {"species": "Chinstrap", "island": "Dream", "bill_length_mm": "46.5", "bill_depth_mm": "17.9",
             "flipper_length_mm": "195", "body_mass_g": "3650", "sex": "MALE", "year": "2008"}
        ]

    def test_avg_body_mass_by_species_and_sex(self):
        result = avg_body_mass_by_species_and_sex(self.sample_data)
        self.assertIn("Adelie (MALE)", result)

    def test_avg_bill_length_by_island_and_year(self):
        result = avg_bill_length_by_island_and_year(self.sample_data)
        self.assertTrue(all(isinstance(v, float) for v in result.values()))

    def test_avg_flipper_length_by_species_and_island(self):
        result = avg_flipper_length_by_species_and_island(self.sample_data)
        self.assertIn("Gentoo (Biscoe)", result)

    def test_body_mass_difference_by_sex_and_island(self):
        result = body_mass_difference_by_sex_and_island(self.sample_data)
        self.assertIn("Torgersen", result)

    def test_bill_depth_vs_flipper_length_by_species(self):
        result = bill_depth_vs_flipper_length_by_species(self.sample_data)
        self.assertIn("Adelie", result)

    def test_avg_bill_length_by_year_and_sex(self):
        result = avg_bill_length_by_year_and_sex(self.sample_data)
        self.assertIn("2007 (MALE)", result)

if __name__ == "__main__":
    main()               # runs analysis and writes the TXT
    print("\nRunning unit tests...\n")
    unittest.main(argv=[''], verbosity=2, exit=False)
