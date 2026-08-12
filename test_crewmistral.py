# test_crewmistral.py
"""
Tests for CrewMistral module.
"""

import unittest
from crewmistral import CrewMistral

class TestCrewMistral(unittest.TestCase):
    """Test cases for CrewMistral class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CrewMistral()
        self.assertIsInstance(instance, CrewMistral)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CrewMistral()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
