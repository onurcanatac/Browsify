import unittest
from PyQt5.QtWidgets import QApplication
from main import main

class TestBrowsifyApplication(unittest.TestCase):
    def setUp(self):
        # Initialize the application instance for testing
        self.app = QApplication([])

    def tearDown(self):
        # Clean up resources after each test
        del self.app

    def test_application_runs(self):
        # Test if the application runs without errors
        main() 

if __name__ == '__main__':
    unittest.main()
