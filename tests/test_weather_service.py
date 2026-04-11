from unittest.mock import Mock, patch

import pytest

from weather_service import get_weather


def test_get_weather_returns_dummy_data_from_mocked_api():
    location = "madrid"
    dummy_payload = {
        "location": location,
        "temperature": 22,
        "condition": "Sunny",
    }

    mocked_response = Mock()
    mocked_response.json.return_value = dummy_payload

    with patch("weather_service.requests.get", return_value=mocked_response) as mock_get:
        result = get_weather(location)

    mock_get.assert_called_once_with(
        "https://api.weather.com/v3/weather/madrid")
    assert result == dummy_payload


def test_get_weather_propagates_json_decoding_errors():
    mocked_response = Mock()
    mocked_response.json.side_effect = ValueError("Invalid JSON")

    with patch("weather_service.requests.get", return_value=mocked_response):
        with pytest.raises(ValueError, match="Invalid JSON"):
            get_weather("bogota")
