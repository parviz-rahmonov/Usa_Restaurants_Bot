import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from data import restaurants as store


class PersistenceTests(unittest.TestCase):
    def test_save_and_reload(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "db.json"
            original = copy.deepcopy(store.RESTAURANTS)
            try:
                with patch.object(store, "DB_PATH", path):
                    store.save()
                    self.assertEqual(json.loads(path.read_text(encoding="utf-8")), original)
                    self.assertEqual(store._load(), original)
                    self.assertFalse(list(Path(temp).glob("*.tmp")))
            finally:
                store.RESTAURANTS.clear()
                store.RESTAURANTS.update(original)

    def test_invalid_json_does_not_silently_reset(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "db.json"
            path.write_text("{invalid", encoding="utf-8")
            with patch.object(store, "DB_PATH", path):
                with self.assertRaises(RuntimeError):
                    store._load()


if __name__ == "__main__":
    unittest.main()
