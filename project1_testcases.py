import unittest
from penguins_analysis import (  # replace with your filename (without .py)
    avg_body_mass_by_species_and_sex,
    avg_bill_length_by_island_and_year,
    avg_flipper_length_by_species_and_island,
    body_mass_difference_by_sex_and_island,
    bill_depth_vs_flipper_length_by_species,
    avg_bill_length_by_year_and_sex
)

class TestPenguinFunctions(unittest.TestCase):

    def setUp(self):
        self.data = [
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
        result = avg_body_mass_by_species_and_sex(self.data)
        self.assertIn("Adelie (MALE)", result)
        self.assertIn("Adelie (FEMALE)", result)
        self.assertEqual(result["Adelie (MALE)"], 3750.0)
        self.assertTrue(all(isinstance(v, float) for v in result.values()))

    def test_avg_bill_length_by_island_and_year(self):
        result = avg_bill_length_by_island_and_year(self.data)
        self.assertIn("Torgersen (2007)", result)
        self.assertTrue(all(isinstance(v, float) for v in result.values()))
        self.assertEqual(result["Torgersen (2007)"], round((39.1 + 39.5) / 2, 2))
        self.assertEqual(len(result), 3)

    def test_avg_flipper_length_by_species_and_island(self):
        result = avg_flipper_length_by_species_and_island(self.data)
        self.assertIn("Gentoo (Biscoe)", result)
        self.assertIn("Adelie (Torgersen)", result)
        self.assertEqual(result["Adelie (Torgersen)"], round((181 + 186)/2, 2))
        self.assertTrue(all(isinstance(v, float) for v in result.values()))

    def test_body_mass_difference_by_sex_and_island(self):
        result = body_mass_difference_by_sex_and_island(self.data)
        self.assertIn("Torgersen", result)
        self.assertIsInstance(result, dict)
        self.assertEqual(result["Torgersen"], 3750 - 3800)
        self.assertTrue(all(isinstance(v, float) or isinstance(v, int) for v in result.values()))

    def test_bill_depth_vs_flipper_length_by_species(self):
        result = bill_depth_vs_flipper_length_by_species(self.data)
        self.assertIn("Adelie", result)
        self.assertIn("Gentoo", result)
        self.assertIn("avg_bill_depth", result["Adelie"])
        self.assertIn("avg_flipper_length", result["Adelie"])