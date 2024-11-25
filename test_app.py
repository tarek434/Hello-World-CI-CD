import unittest
from app import hello_world

class TestApp(unittest.TestCase):
    def test_help_world(self):
        self.assertAlmostEqual(hello_world(), "Hello World")

if __name__ == "__main__":
    unittest.main()