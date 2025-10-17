import unittest
import pytest
from config.config import get_api_key

class TestConfig(unittest.TestCase):
    """Unit tests for the configuration module, specifically testing the get_api_key function."""

    @pytest.fixture(autouse=True)
    def setUP(self, monkeypatch):
        """Set up the test environment by initializing the monkeypatch fixture.

        Args:
            monkeypatch: Pytest fixture for modifying environment variables during testing.
        """
        self.monkeypatch = monkeypatch

    def test_config_success_get_api_key(self):
        """Test that get_api_key returns the correct API key when the environment variable is set."""
        self.monkeypatch.setenv("API_KEY", "1234")
        api_key = get_api_key()
        self.assertEqual(api_key, "1234")

    def test_config_failed_get_api_key(self):
        """Test that get_api_key returns None when the API_KEY environment variable is not set."""
        self.monkeypatch.delenv("API_KEY", raising=False)
        api_key = get_api_key()
        self.assertEqual(api_key, None)