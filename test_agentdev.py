# test_agentdev.py
"""
Tests for AgentDev module.
"""

import unittest
from agentdev import AgentDev

class TestAgentDev(unittest.TestCase):
    """Test cases for AgentDev class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentDev()
        self.assertIsInstance(instance, AgentDev)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentDev()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
