# test_primespectrum.py
"""
Tests for PrimeSpectrum module.
"""

import unittest
from primespectrum import PrimeSpectrum

class TestPrimeSpectrum(unittest.TestCase):
    """Test cases for PrimeSpectrum class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeSpectrum()
        self.assertIsInstance(instance, PrimeSpectrum)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeSpectrum()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
