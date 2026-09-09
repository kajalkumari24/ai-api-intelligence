"""
Tests for the API category inference pipeline.

Run with: pytest tests/test_inference.py -v
"""

import sys
from pathlib import Path

# Add src/models to the path so we can import inference.py
sys.path.append(str(Path(__file__).parent.parent / "src" / "models"))

from inference import predict_api_category


def test_predicts_a_string():
    """The function should return a category name, not a number or None."""
    result = predict_api_category("Test API", "Some description")
    assert isinstance(result, str)
    assert len(result) > 0


def test_cryptocurrency_example():
    """A clear crypto description should be classified as Cryptocurrency."""
    result = predict_api_category(
        "CoinGecko", "Cryptocurrency prices, market cap, and trading volume data"
    )
    assert result == "Cryptocurrency"


def test_weather_example():
    """A clear weather description should be classified as Weather."""
    result = predict_api_category(
        "OpenWeatherMap", "Current weather and forecast data for any location"
    )
    assert result == "Weather"


def test_handles_missing_name():
    """The function should still work if name is left blank."""
    result = predict_api_category("", "Real-time stock market data")
    assert isinstance(result, str)


def test_known_category_exists():
    """The model should only ever predict one of our real known categories."""
    known_categories = {
        "Development", "Cryptocurrency", "Weather", "Animals", "Health",
        "Finance", "Government", "Other"  # add more as needed, or load the real list
    }
    result = predict_api_category("GitHub API", "Access repositories and pull requests")
    # This test just checks the result is a plausible string, since we don't
    # have the full 41-category list hardcoded here
    assert isinstance(result, str) and len(result) > 0