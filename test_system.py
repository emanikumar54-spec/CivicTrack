
import unittest
import tempfile
from pathlib import Path

import database
from priority_engine import calculate_priority


class TestCivicTrack(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_path = database.DATABASE_PATH
        database.DATABASE_PATH = Path(self.temp_dir.name) / "test.db"
        database.initialize_database()

        self.sample_data = {
            "name": "Test User",
            "phone": "9876543210",
            "category": "Road Damage",
            "location": "Hyderabad",
            "description": "Damaged road near main street",
            "severity": 5,
            "people_affected": 500,
            "safety_impact": 5,
            "priority": "Critical",
            "priority_score": 110
        }

    def tearDown(self):
        database.DATABASE_PATH = self.original_path
        import gc
        gc.collect()
        self.temp_dir.cleanup()

    def test_database_initialization(self):
        self.assertEqual(len(database.get_all_complaints()), 0)

    def test_priority_calculation(self):
        result = calculate_priority(5, 500, 5, "Road Damage")
        self.assertEqual(result["priority"], "Critical")
        self.assertEqual(result["priority_score"], 110)

    def test_add_complaint(self):
        complaint_id = database.add_complaint(self.sample_data)
        self.assertTrue(complaint_id.startswith("CIVIC-"))
        complaint = database.get_complaint(complaint_id)
        self.assertIsNotNone(complaint)
        self.assertEqual(complaint["name"], "Test User")

    def test_update_complaint_status(self):
        complaint_id = database.add_complaint(self.sample_data)
        result = database.update_complaint_status(complaint_id, "In Progress")
        complaint = database.get_complaint(complaint_id)
        self.assertTrue(result)
        self.assertEqual(complaint["status"], "In Progress")

    def test_delete_complaint(self):
        complaint_id = database.add_complaint(self.sample_data)
        result = database.delete_complaint(complaint_id)
        self.assertTrue(result)
        self.assertIsNone(database.get_complaint(complaint_id))

    def test_invalid_complaint_lookup(self):
        self.assertIsNone(database.get_complaint("INVALID-ID"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
